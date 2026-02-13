try:
    from ..utils import AnyType
except ImportError:
    from utils import AnyType

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
