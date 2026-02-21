import math

class MathAdd:
    """
    A simple node that adds two integers.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "a": ("INT", {"default": 0, "min": -1000000, "max": 1000000, "step": 1}),
                "b": ("INT", {"default": 0, "min": -1000000, "max": 1000000, "step": 1}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("result",)

    FUNCTION = "add"

    # OUTPUT_NODE = False

    CATEGORY = "h2nodes/Math"

    def add(self, a: int, b: int) -> tuple[int]:
        """
        Adds two integers.

        Args:
            a (int): The first integer.
            b (int): The second integer.

        Returns:
            tuple[int]: A tuple containing the sum of a and b.
        """
        return (a + b,)

class MathSubtract:
    """
    A simple node that subtracts two integers.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "a": ("INT", {"default": 0, "min": -1000000, "max": 1000000, "step": 1}),
                "b": ("INT", {"default": 0, "min": -1000000, "max": 1000000, "step": 1}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("result",)
    FUNCTION = "subtract"
    CATEGORY = "h2nodes/Math"

    def subtract(self, a: int, b: int) -> tuple[int]:
        return (a - b,)

class MathMultiply:
    """
    A simple node that multiplies two integers.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "a": ("INT", {"default": 0, "min": -1000000, "max": 1000000, "step": 1}),
                "b": ("INT", {"default": 0, "min": -1000000, "max": 1000000, "step": 1}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("result",)
    FUNCTION = "multiply"
    CATEGORY = "h2nodes/Math"

    def multiply(self, a: int, b: int) -> tuple[int]:
        return (a * b,)

class MathDivide:
    """
    A simple node that divides two integers.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "a": ("INT", {"default": 0, "min": -1000000, "max": 1000000, "step": 1}),
                "b": ("INT", {"default": 1, "min": -1000000, "max": 1000000, "step": 1}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("result",)
    FUNCTION = "divide"
    CATEGORY = "h2nodes/Math"

    def divide(self, a: int, b: int) -> tuple[float]:
        if b == 0:
            return (0.0,)
        return (float(a) / float(b),)

class MathModulus:
    """
    A simple node that calculates the modulus of two integers.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "a": ("INT", {"default": 0, "min": -1000000, "max": 1000000, "step": 1}),
                "b": ("INT", {"default": 1, "min": -1000000, "max": 1000000, "step": 1}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("result",)
    FUNCTION = "modulus"
    CATEGORY = "h2nodes/Math"

    def modulus(self, a: int, b: int) -> tuple[int]:
        if b == 0:
            return (0,)
        return (a % b,)

class MathExpression:
    """
    A node that evaluates a mathematical expression using a, b, and c as variables.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "expression": ("STRING", {"multiline": True, "default": "a + b"}),
                "a": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "b": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "c": ("FLOAT", {"default": 0.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT",)
    RETURN_NAMES = ("result_int", "result_float",)
    FUNCTION = "evaluate"
    CATEGORY = "h2nodes/Math"

    def evaluate(self, expression: str, a: float, b: float, c: float) -> tuple[int, float]:
        # Create a safe environment with math functions
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names.update({
            "a": a,
            "b": b,
            "c": c,
            "abs": abs,
            "min": min,
            "max": max,
            "round": round,
            "sum": sum,
            "pow": pow,
        })

        try:
            # We strictly limit builtins to avoid access to dangerous functions like __import__
            result = eval(expression, {"__builtins__": {}}, allowed_names)

            if isinstance(result, (int, float)):
                return (int(result), float(result),)
            elif isinstance(result, bool):
                val = 1 if result else 0
                return (val, float(val),)
            else:
                 # Try to cast whatever it is
                return (int(result), float(result),)
        except Exception as e:
            print(f"[MathExpression] Error evaluating '{expression}': {e}")
            return (0, 0.0,)

class MathClamp:
    """
    A node that clamps a value between a minimum and maximum.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "min": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "max": ("FLOAT", {"default": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT",)
    RETURN_NAMES = ("result_int", "result_float",)
    FUNCTION = "clamp"
    CATEGORY = "h2nodes/Math"

    def clamp(self, value: float, min: float, max: float) -> tuple[int, float]:
        # Using simple if statements to avoid shadowing builtins issues
        res = value
        if res < min:
            res = min
        if res > max:
            res = max

        return (int(res), float(res))

class MathRemap:
    """
    A node that remaps a value from one range to another.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "input_min": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "input_max": ("FLOAT", {"default": 1.0, "step": 0.01}),
                "output_min": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "output_max": ("FLOAT", {"default": 1.0, "step": 0.01}),
                "clamp": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT",)
    RETURN_NAMES = ("result_int", "result_float",)
    FUNCTION = "remap"
    CATEGORY = "h2nodes/Math"

    def remap(self, value: float, input_min: float, input_max: float, output_min: float, output_max: float, clamp: bool) -> tuple[int, float]:
        if input_min == input_max:
             return (int(output_min), float(output_min))

        normalized = (value - input_min) / (input_max - input_min)
        mapped = output_min + (normalized * (output_max - output_min))

        if clamp:
            if output_min < output_max:
                if mapped < output_min: mapped = output_min
                if mapped > output_max: mapped = output_max
            else:
                if mapped < output_max: mapped = output_max
                if mapped > output_min: mapped = output_min

        return (int(mapped), float(mapped))
