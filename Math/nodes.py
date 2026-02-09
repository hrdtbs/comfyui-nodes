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
