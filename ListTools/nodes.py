try:
    from ..utils import AnyType
except ImportError:
    from utils import AnyType

class ListGetItem:
    """
    Returns the item at the specified index from a list.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "list_input": (AnyType("*"), {"forceInput": True}),
                "index": ("INT", {"default": 0, "min": -100000, "max": 100000}),
            }
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("item",)
    FUNCTION = "get_item"
    CATEGORY = "h2nodes/ListTools"

    def get_item(self, list_input: list, index: list[int]) -> tuple:
        # INPUT_IS_LIST=True, so 'index' is a list of integers (batch/widget values).
        # We take the first one.
        idx = index[0] if isinstance(index, list) and index else 0

        try:
            return (list_input[idx],)
        except IndexError:
            print(f"[ListGetItem] Index {idx} out of range for list of length {len(list_input)}. Returning None.")
            return (None,)

class ListLength:
    """
    Returns the length of a list.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "list_input": (AnyType("*"), {"forceInput": True}),
            }
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("length",)
    FUNCTION = "get_length"
    CATEGORY = "h2nodes/ListTools"

    def get_length(self, list_input: list) -> tuple[int]:
        return (len(list_input),)
