class SimpleMathAdd:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
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

    CATEGORY = "SimpleMath"

    def add(self, a, b):
        return (a + b,)
