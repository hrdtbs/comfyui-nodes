import torch
import numpy as np
import cv2
import mediapipe as mp
import math

# Try importing comfy modules, but don't fail if they are missing (for local testing)
try:
    import comfy.utils
    import comfy.model_management
    import nodes
except ImportError:
    pass

class AnatomyGuardUtils:
    @staticmethod
    def tensor_to_cv2(image: torch.Tensor) -> np.ndarray:
        """
        Converts a ComfyUI image tensor (RGB) to an OpenCV image (BGR).
        """
        # image: [B, H, W, C] or [H, W, C]
        if len(image.shape) == 4:
            image = image[0]

        # Convert from torch to numpy
        image_np = image.cpu().numpy()

        # Convert from RGB (ComfyUI) to BGR (OpenCV)
        # Check if ranges are 0-1 or 0-255
        if image_np.max() <= 1.0:
            image_np = (image_np * 255).astype(np.uint8)
        else:
            image_np = image_np.astype(np.uint8)

        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        return image_bgr

    @staticmethod
    def cv2_to_tensor(image_bgr: np.ndarray) -> torch.Tensor:
        """
        Converts an OpenCV image (BGR) to a ComfyUI image tensor (RGB).
        """
        # image_bgr: [H, W, C] uint8
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        image_np = image_rgb.astype(np.float32) / 255.0
        # Add batch dimension
        return torch.from_numpy(image_np).unsqueeze(0)

class AnatomyDetectionMesh:
    """
    Node that detects hands using MediaPipe.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("HAND_DATA",)
    RETURN_NAMES = ("hand_data",)
    FUNCTION = "detect"
    CATEGORY = "h2nodes/AnatomyGuard"

    def detect(self, image: torch.Tensor) -> tuple[list]:
        """
        Runs MediaPipe Hands on the input image.

        Args:
            image (torch.Tensor): The input image.

        Returns:
            tuple[list]: A tuple containing a list of hand data dictionaries.
        """
        mp_hands = mp.solutions.hands

        # Convert to BGR first (as per Utils) then RGB for MediaPipe
        image_bgr = AnatomyGuardUtils.tensor_to_cv2(image)
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

        height, width, _ = image_bgr.shape

        with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=2,
            min_detection_confidence=0.5
        ) as hands:
            results = hands.process(image_rgb)

            hands_data = []

            if results.multi_hand_landmarks:
                for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    # Handedness
                    label = "Unknown"
                    score = 0.0
                    if results.multi_handedness:
                        # Ensure index is within bounds (sometimes mismatch happens in MP?)
                        if i < len(results.multi_handedness):
                             label = results.multi_handedness[i].classification[0].label
                             score = results.multi_handedness[i].classification[0].score

                    landmarks = []
                    for lm in hand_landmarks.landmark:
                        landmarks.append({'x': lm.x, 'y': lm.y, 'z': lm.z})

                    w_landmarks = []
                    if results.multi_hand_world_landmarks:
                         if i < len(results.multi_hand_world_landmarks):
                            for lm in results.multi_hand_world_landmarks[i].landmark:
                                w_landmarks.append({'x': lm.x, 'y': lm.y, 'z': lm.z})

                    hands_data.append({
                        "landmarks": landmarks,
                        "world_landmarks": w_landmarks,
                        "label": label,
                        "score": score,
                        "image_width": width,
                        "image_height": height
                    })

            return (hands_data,)

class AnatomyLogicEvaluator:
    """
    Node that evaluates the detected hand data against anatomical constraints.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "hand_data": ("HAND_DATA",),
                "threshold": ("FLOAT", {"default": 0.05, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("BOOLEAN", "MASK")
    RETURN_NAMES = ("condition", "mask")
    FUNCTION = "evaluate"
    CATEGORY = "h2nodes/AnatomyGuard"

    def evaluate(self, hand_data: list, threshold: float) -> tuple[bool, torch.Tensor]:
        """
        Evaluates hand geometry validity.

        Args:
            hand_data (list): The list of detected hands.
            threshold (float): Sensitivity threshold for checks.

        Returns:
            tuple[bool, torch.Tensor]: A tuple of (is_valid, error_mask).
        """
        # Default: All good (True)
        is_valid = True

        if not hand_data:
            # No hands, assume valid
            empty_mask = torch.zeros((1, 64, 64), dtype=torch.float32)
            return (True, empty_mask)

        width = hand_data[0]["image_width"]
        height = hand_data[0]["image_height"]

        mask_np = np.zeros((height, width), dtype=np.uint8)

        for hand in hand_data:
            hand_valid = True
            landmarks = hand["landmarks"]

            # 1. ROM Check (Simple example: Sharp Angles)
            fingers = [
                (5, 6, 7, 8), # Index
                (9, 10, 11, 12), # Middle
                (13, 14, 15, 16), # Ring
                (17, 18, 19, 20)  # Pinky
            ]

            for f_indices in fingers:
                mcp = landmarks[f_indices[0]]
                pip = landmarks[f_indices[1]]
                dip = landmarks[f_indices[2]]

                # Vectors
                v1 = np.array([pip['x'] - mcp['x'], pip['y'] - mcp['y'], pip['z'] - mcp['z']])
                v2 = np.array([dip['x'] - pip['x'], dip['y'] - pip['y'], dip['z'] - pip['z']])

                v1_norm = np.linalg.norm(v1)
                v2_norm = np.linalg.norm(v2)

                if v1_norm > 0 and v2_norm > 0:
                    v1_u = v1 / v1_norm
                    v2_u = v2 / v2_norm

                    dot = np.dot(v1_u, v2_u)
                    # Clip to handle float errors
                    angle = np.arccos(np.clip(dot, -1.0, 1.0))

                    # If angle > threshold (e.g., 90 degrees bend = pi/2 = 1.57)
                    # This is just a heuristic. Real ROM is complex.
                    # We use a loose threshold.
                    if angle > 2.0:
                         hand_valid = False

            # 2. Adhesion Check (Distance between adjacent PIP joints)
            # Index(6) vs Middle(10)
            idx_pip = landmarks[6]
            mid_pip = landmarks[10]
            dist = math.sqrt((idx_pip['x']-mid_pip['x'])**2 + (idx_pip['y']-mid_pip['y'])**2)

            # Threshold relative to normalized coords (0-1).
            # 0.05 is 5% of image dimension.
            if dist < threshold * 0.5:
                hand_valid = False

            if not hand_valid:
                is_valid = False
                # Draw mask for this hand
                points = []
                for lm in landmarks:
                    px = int(lm['x'] * width)
                    py = int(lm['y'] * height)
                    points.append((px, py))

                points_np = np.array(points, dtype=np.int32)
                if len(points_np) > 0:
                    hull = cv2.convexHull(points_np)
                    cv2.fillConvexPoly(mask_np, hull, 255)

        # Convert mask to tensor [1, H, W]
        mask_tensor = torch.from_numpy(mask_np.astype(np.float32) / 255.0).unsqueeze(0)

        return (is_valid, mask_tensor)

class IterativeAnatomyRefiner:
    """
    Node that attempts to fix invalid anatomy using inpainting.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "model": ("MODEL",),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0}),
            },
            "optional": {
                 "vae": ("VAE",),
                 "positive": ("CONDITIONING",),
                 "negative": ("CONDITIONING",),
                 "controlnet_stack": ("CONTROLNET_STACK",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("refined_image",)
    FUNCTION = "refine"
    CATEGORY = "h2nodes/AnatomyGuard"

    def refine(self, image: torch.Tensor, mask: torch.Tensor, model, seed: int, steps: int, cfg: float, denoise: float, vae=None, positive=None, negative=None, controlnet_stack=None) -> tuple[torch.Tensor]:
        """
        Refines the image area defined by the mask.
        """
        # 1. Dilation
        mask_np = mask.cpu().numpy()
        if len(mask_np.shape) == 3:
            mask_np = mask_np[0]

        # Dilate
        kernel = np.ones((5,5), np.uint8)
        dilated_mask_np = cv2.dilate(mask_np, kernel, iterations=2)
        # Blur for alpha blending
        blurred_mask_np = cv2.GaussianBlur(dilated_mask_np, (21, 21), 0)

        dilated_mask_tensor = torch.from_numpy(dilated_mask_np).unsqueeze(0)
        blurred_mask_tensor = torch.from_numpy(blurred_mask_np).unsqueeze(0) # [1, H, W]

        refined_image = image # Default fallback

        # 2. Generation (Inpaint)
        # Check if ComfyUI nodes are available and inputs provided
        if vae is not None and positive is not None and negative is not None and 'nodes' in globals():
            try:
                # 1. Encode
                vae_enc = nodes.VAEEncode()
                latent = vae_enc.encode(vae, image)[0]

                # 2. Apply Mask
                mask_node = nodes.SetLatentNoiseMask()
                latent_masked = mask_node.set_mask(samples=latent, mask=dilated_mask_tensor)[0]

                # 3. KSampler
                ksampler = nodes.KSampler()
                # Defaults: sampler_name="euler", scheduler="normal"
                latent_out = ksampler.sample(model, seed, steps, cfg, "euler", "normal", positive, negative, latent_masked, denoise=denoise)[0]

                # 4. Decode
                vae_dec = nodes.VAEDecode()
                refined_image = vae_dec.decode(vae, latent_out)[0]

            except Exception as e:
                print(f"AnatomyGuard Refiner Generation Failed: {e}")

        # 3. Alpha Blending
        # output = original * (1 - alpha) + refined * alpha
        # Ensure alpha has channels dimension: [1, H, W, 1]
        alpha = blurred_mask_tensor.unsqueeze(-1)

        # Handle broadcasting if image has batch > 1 (not handled here, assuming single image/first image logic for now)
        # Refined image from VAE is [1, H, W, 3] usually.
        # Original image might be [B, H, W, 3].

        if refined_image.shape[1:] != image.shape[1:]:
             # Simple resize fallback if dimensions mismatch (rare if same VAE)
             # Or if batch size mismatch, just take first
             pass

        # Expand alpha to match refined_image if needed
        if alpha.shape[1] != refined_image.shape[1] or alpha.shape[2] != refined_image.shape[2]:
            # Resize alpha?
            # For this simplified implementation, assume they match.
            pass

        output_image = image * (1.0 - alpha) + refined_image * alpha

        return (output_image,)
