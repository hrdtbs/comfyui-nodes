from .nodes import ListGetItem, ListLength

NODE_CLASS_MAPPINGS = {
    "ListGetItem": ListGetItem,
    "ListLength": ListLength,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ListGetItem": "List Get Item",
    "ListLength": "List Length",
}
