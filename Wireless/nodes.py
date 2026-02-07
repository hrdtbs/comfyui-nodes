from .utils import AnyType

class Wireless:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "data": (AnyType("*"),),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "func"
    CATEGORY = "h2nodes/Wireless"
    OUTPUT_NODE = True

    def func(self, **kwargs):
        return ()
