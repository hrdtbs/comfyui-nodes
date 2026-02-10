from .nodes import MathAdd, MathSubtract, MathMultiply, MathDivide, MathModulus

NODE_CLASS_MAPPINGS = {
    "MathAdd": MathAdd,
    "MathSubtract": MathSubtract,
    "MathMultiply": MathMultiply,
    "MathDivide": MathDivide,
    "MathModulus": MathModulus
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MathAdd": "Math Add",
    "MathSubtract": "Math Subtract",
    "MathMultiply": "Math Multiply",
    "MathDivide": "Math Divide",
    "MathModulus": "Math Modulus"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
