import torch
import math

class ImageProperties:
    """
    A node that extracts properties from an image tensor.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("INT", "INT", "FLOAT", "INT")
    RETURN_NAMES = ("width", "height", "aspect_ratio", "batch_size")
    FUNCTION = "get_properties"
    CATEGORY = "h2nodes/ImageTools"

    def get_properties(self, image: torch.Tensor) -> tuple[int, int, float, int]:
        """
        Extracts width, height, aspect ratio, and batch size from an image tensor.

        Args:
            image (torch.Tensor): The input image tensor [B, H, W, C].

        Returns:
            tuple: (width, height, aspect_ratio, batch_size)
        """
        # image shape is [Batch, Height, Width, Channels]
        # B = 0, H = 1, W = 2, C = 3
        batch_size = image.shape[0]
        height = image.shape[1]
        width = image.shape[2]

        aspect_ratio = float(width) / float(height) if height != 0 else 0.0

        return (width, height, aspect_ratio, batch_size)


class ImageResizeCalculator:
    """
    A node that calculates new dimensions based on a scale factor.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 1, "max": 10000}),
                "height": ("INT", {"default": 512, "min": 1, "max": 10000}),
                "scale_factor": ("FLOAT", {"default": 1.0, "min": 0.01, "max": 100.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "calculate_new_size"
    CATEGORY = "h2nodes/ImageTools"

    def calculate_new_size(self, width: int, height: int, scale_factor: float) -> tuple[int, int]:
        """
        Calculates new width and height based on the scale factor.

        Args:
            width (int): Original width.
            height (int): Original height.
            scale_factor (float): The scaling factor.

        Returns:
            tuple: (new_width, new_height)
        """
        new_width = int(round(width * scale_factor))
        new_height = int(round(height * scale_factor))

        return (new_width, new_height)
