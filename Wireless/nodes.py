class AnyType(str):
    """
    A special type that compares equal to any other type.
    This is used to accept any input in ComfyUI nodes.
    """
    def __ne__(self, __value: object) -> bool:
        return False

    def __eq__(self, __value: object) -> bool:
        return True

    def __str__(self) -> str:
        return self

class Wireless:
    """
    A node that acts as a wireless receiver/broadcaster.
    Input data is automatically connected to matching unconnected inputs in the workflow via Javascript.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "data": (AnyType("*"),),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "func"
    CATEGORY = "h2nodes/Wireless"
    OUTPUT_NODE = True

    def func(self, **kwargs) -> tuple:
        """
        The execution function. Since this node handles connections in the frontend,
        this function does nothing but return an empty tuple.
        """
        return ()
