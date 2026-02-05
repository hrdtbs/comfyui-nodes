import sys
import os
import unittest

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Math.nodes import MathAdd

class TestMath(unittest.TestCase):
    def test_add_basic(self):
        adder = MathAdd()
        result = adder.add(5, 3)
        self.assertEqual(result[0], 8)

    def test_add_negative(self):
        adder = MathAdd()
        result = adder.add(10, -5)
        self.assertEqual(result[0], 5)

        result = adder.add(-5, -3)
        self.assertEqual(result[0], -8)

    def test_add_zero(self):
        adder = MathAdd()
        result = adder.add(10, 0)
        self.assertEqual(result[0], 10)

        result = adder.add(0, 0)
        self.assertEqual(result[0], 0)

    def test_input_types(self):
        input_types = MathAdd.INPUT_TYPES()
        self.assertIn("required", input_types)
        self.assertIn("a", input_types["required"])
        self.assertIn("b", input_types["required"])

if __name__ == '__main__':
    unittest.main()
