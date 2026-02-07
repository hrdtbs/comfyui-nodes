import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock mediapipe before importing nodes because it might be broken in this env or we want full control
mock_mp = MagicMock()
sys.modules["mediapipe"] = mock_mp

# Need to reload or import after mocking
# But since this script runs once, imports happen now.
try:
    import torch
    import numpy as np
    from AnatomyGuard.nodes import AnatomyDetectionMesh, AnatomyLogicEvaluator, IterativeAnatomyRefiner, AnatomyGuardUtils
    IMPORTS_SUCCESS = True
except ImportError:
    # In case import fails for other reasons
    IMPORTS_SUCCESS = False
    pass


class TestAnatomyGuard(unittest.TestCase):
    def setUp(self):
        if not IMPORTS_SUCCESS:
            self.skipTest("Required dependencies (torch, AnatomyGuard) not found")
        # Reset mock configuration if needed
        pass

    def test_utils_conversion(self):
        # Test tensor_to_cv2
        tensor = torch.zeros((1, 100, 100, 3), dtype=torch.float32)
        cv2_img = AnatomyGuardUtils.tensor_to_cv2(tensor)
        self.assertEqual(cv2_img.shape, (100, 100, 3))
        self.assertEqual(cv2_img.dtype, np.uint8)

        # Test cv2_to_tensor
        cv2_img = np.zeros((100, 100, 3), dtype=np.uint8)
        tensor_back = AnatomyGuardUtils.cv2_to_tensor(cv2_img)
        self.assertEqual(tensor_back.shape, (1, 100, 100, 3))
        self.assertEqual(tensor_back.dtype, torch.float32)

    def test_detection_node(self):
        # Configure the global mock_mp to return what we want
        # mp.solutions.hands.Hands(...) -> context manager -> results

        mock_hands_class = mock_mp.solutions.hands.Hands
        mock_instance = mock_hands_class.return_value.__enter__.return_value

        # Mock result
        mock_result = MagicMock()
        lm = MagicMock()
        lm.x, lm.y, lm.z = 0.5, 0.5, 0.0
        hand_landmarks = MagicMock()
        hand_landmarks.landmark = [lm] * 21

        mock_result.multi_hand_landmarks = [hand_landmarks]
        mock_result.multi_handedness = [MagicMock(classification=[MagicMock(label="Right", score=0.9)])]
        mock_result.multi_hand_world_landmarks = [hand_landmarks]

        mock_instance.process.return_value = mock_result

        node = AnatomyDetectionMesh()
        image = torch.zeros((1, 100, 100, 3))

        results = node.detect(image)
        hand_data = results[0]

        self.assertEqual(len(hand_data), 1)
        self.assertEqual(hand_data[0]["label"], "Right")
        self.assertEqual(len(hand_data[0]["landmarks"]), 21)

    def test_evaluator_node_pass(self):
        node = AnatomyLogicEvaluator()

        # Test empty case
        res = node.evaluate([], 0.5)
        self.assertTrue(res[0])

        # Test failure case
        landmarks = [{'x':0,'y':0,'z':0} for _ in range(21)]
        # Make a sharp angle for index finger
        landmarks[5] = {'x':0, 'y':0, 'z':0}
        landmarks[6] = {'x':0, 'y':1, 'z':0}
        landmarks[7] = {'x':0, 'y':0, 'z':0}

        hand_data = [{
            "landmarks": landmarks,
            "image_width": 100,
            "image_height": 100
        }]

        res_fail, mask = node.evaluate(hand_data, 0.5)
        self.assertFalse(res_fail)
        self.assertEqual(mask.shape, (1, 100, 100))

    def test_refiner_node_structure(self):
        node = IterativeAnatomyRefiner()
        image = torch.zeros((1, 100, 100, 3))
        mask = torch.zeros((1, 100, 100))
        model = MagicMock()

        res = node.refine(image, mask, model, seed=0, steps=1, cfg=1.0, denoise=0.5)

        # Should return image
        self.assertEqual(res[0].shape, image.shape)

if __name__ == '__main__':
    unittest.main()
