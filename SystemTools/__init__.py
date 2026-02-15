from .nodes import GetDateString

NODE_CLASS_MAPPINGS = {
    "GetDateString": GetDateString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GetDateString": "Get Date String",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
