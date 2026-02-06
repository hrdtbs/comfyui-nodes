import unittest
from ResolutionSelector.nodes import ResolutionSelector

class TestResolutionSelector(unittest.TestCase):
    def setUp(self):
        self.node = ResolutionSelector()

    def test_select_resolution(self):
        # Test parsing
        cases = [
            ("SD1.5 - 512x512 (1:1)", 512, 512),
            ("SDXL / Illustrious - 1152x896 (9:7)", 1152, 896),
            ("SDXL / Illustrious - 640x1536 (5:12)", 640, 1536),
        ]

        for res_str, expected_w, expected_h in cases:
            w, h = self.node.select_resolution(res_str)
            self.assertEqual(w, expected_w, f"Failed for {res_str}")
            self.assertEqual(h, expected_h, f"Failed for {res_str}")

    def test_invalid_input(self):
        # Test robustness
        w, h = self.node.select_resolution("Invalid Input")
        self.assertEqual(w, 0)
        self.assertEqual(h, 0)

if __name__ == '__main__':
    unittest.main()
