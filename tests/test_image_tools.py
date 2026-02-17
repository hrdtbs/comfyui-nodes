import unittest
from unittest.mock import MagicMock
import sys
import os

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Attempt to import globally for the test class, but carefully
try:
    import torch
except ImportError:
    # Mock torch for this test file execution if not available
    sys.modules["torch"] = MagicMock()

from ImageTools.nodes import ImageProperties, ImageResizeCalculator, ImageScaleToTotalPixels

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

    def test_scale_to_total_pixels(self):
        node = ImageScaleToTotalPixels()

        # 1MP target from 512x512
        # 512*512 = 262144
        # 1MP = 1000000
        # scale = sqrt(1000000/262144) = sqrt(3.814697) = 1.953125
        # 512 * 1.953125 = 1000
        w, h, s = node.calculate_new_size(512, 512, 1.0)
        self.assertEqual(w, 1000)
        self.assertEqual(h, 1000)

        # 1MP target from 100x200 (aspect 0.5)
        # 20000 pixels
        # scale = sqrt(1000000/20000) = sqrt(50) = 7.0710678
        # 100 * 7.071... = 707
        # 200 * 7.071... = 1414
        w, h, s = node.calculate_new_size(100, 200, 1.0)
        self.assertEqual(w, 707)
        self.assertEqual(h, 1414)

        # Zero pixels
        w, h, s = node.calculate_new_size(0, 100, 1.0)
        self.assertEqual(w, 0)
        self.assertEqual(h, 100)
        self.assertEqual(s, 1.0)

        # 0.25MP target from 1000x1000
        # 1000*1000 = 1000000
        # 0.25MP = 250000
        # scale = sqrt(0.25) = 0.5
        w, h, s = node.calculate_new_size(1000, 1000, 0.25)
        self.assertEqual(w, 500)
        self.assertEqual(h, 500)

if __name__ == '__main__':
    unittest.main()
