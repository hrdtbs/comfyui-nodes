
class AnyType(str):
    """A special type that compares equal to any other type.
    This is used to accept any input in ComfyUI nodes.
    """
    def __ne__(self, __value: object) -> bool:
        return False

    def __eq__(self, __value: object) -> bool:
        return True

    def __str__(self):
        return self

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
