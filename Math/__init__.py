from .nodes import MathAdd, MathSubtract, MathMultiply, MathDivide, MathModulus, MathExpression

NODE_CLASS_MAPPINGS = {
    "MathAdd": MathAdd,
    "MathSubtract": MathSubtract,
    "MathMultiply": MathMultiply,
    "MathDivide": MathDivide,
    "MathModulus": MathModulus,
    "MathExpression": MathExpression
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MathAdd": "Math Add",
    "MathSubtract": "Math Subtract",
    "MathMultiply": "Math Multiply",
    "MathDivide": "Math Divide",
    "MathModulus": "Math Modulus",
    "MathExpression": "Math Expression"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
