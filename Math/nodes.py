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
