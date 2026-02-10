import sys
import os
import unittest

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Math.nodes import MathAdd, MathSubtract, MathMultiply, MathDivide, MathModulus

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

    def test_subtract_basic(self):
        subtractor = MathSubtract()
        result = subtractor.subtract(10, 3)
        self.assertEqual(result[0], 7)

    def test_subtract_negative(self):
        subtractor = MathSubtract()
        result = subtractor.subtract(10, -5)
        self.assertEqual(result[0], 15)

        result = subtractor.subtract(-5, -3)
        self.assertEqual(result[0], -2)

    def test_multiply_basic(self):
        multiplier = MathMultiply()
        result = multiplier.multiply(5, 3)
        self.assertEqual(result[0], 15)

    def test_multiply_zero(self):
        multiplier = MathMultiply()
        result = multiplier.multiply(5, 0)
        self.assertEqual(result[0], 0)

    def test_multiply_negative(self):
        multiplier = MathMultiply()
        result = multiplier.multiply(5, -3)
        self.assertEqual(result[0], -15)

    def test_divide_basic(self):
        divider = MathDivide()
        result = divider.divide(10, 2)
        self.assertEqual(result[0], 5.0)

    def test_divide_float(self):
        divider = MathDivide()
        result = divider.divide(5, 2)
        self.assertEqual(result[0], 2.5)

    def test_divide_zero(self):
        divider = MathDivide()
        result = divider.divide(10, 0)
        self.assertEqual(result[0], 0.0)

    def test_modulus_basic(self):
        moduler = MathModulus()
        result = moduler.modulus(10, 3)
        self.assertEqual(result[0], 1)

    def test_modulus_zero(self):
        moduler = MathModulus()
        result = moduler.modulus(10, 0)
        self.assertEqual(result[0], 0)

    def test_input_types(self):
        input_types = MathAdd.INPUT_TYPES()
        self.assertIn("required", input_types)
        self.assertIn("a", input_types["required"])
        self.assertIn("b", input_types["required"])

if __name__ == '__main__':
    unittest.main()
