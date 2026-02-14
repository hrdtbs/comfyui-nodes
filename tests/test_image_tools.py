import unittest
from unittest.mock import MagicMock
import sys
import os

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock torch before importing ImageTools
mock_torch = MagicMock()
sys.modules["torch"] = mock_torch

from ImageTools.nodes import ImageProperties, ImageResizeCalculator

class TestImageTools(unittest.TestCase):
    def test_image_properties(self):
        node = ImageProperties()

        # Mock tensor [Batch, Height, Width, Channels]
        mock_image = MagicMock()
        mock_image.shape = [2, 512, 768, 3] # B=2, H=512, W=768

        # Function returns tuple: (width, height, aspect_ratio, batch_size)
        res = node.get_properties(mock_image)

        self.assertEqual(res[0], 768) # width
        self.assertEqual(res[1], 512) # height
        self.assertEqual(res[2], 1.5) # aspect ratio (768/512 = 1.5)
        self.assertEqual(res[3], 2)   # batch size

    def test_image_properties_zero_height(self):
        # Edge case: height is 0
        node = ImageProperties()
        mock_image = MagicMock()
        mock_image.shape = [1, 0, 100, 3]

        res = node.get_properties(mock_image)
        self.assertEqual(res[1], 0)
        self.assertEqual(res[2], 0.0)

    def test_resize_calculator(self):
        node = ImageResizeCalculator()

        # Standard scaling
        w, h = node.calculate_new_size(100, 100, 1.5)
        self.assertEqual(w, 150)
        self.assertEqual(h, 150)

        # Rounding check
        # 100 * 1.55 = 155.0
        w, h = node.calculate_new_size(100, 100, 1.55)
        self.assertEqual(w, 155)
        self.assertEqual(h, 155)

        # Scale down
        w, h = node.calculate_new_size(100, 200, 0.5)
        self.assertEqual(w, 50)
        self.assertEqual(h, 100)

if __name__ == '__main__':
    unittest.main()
