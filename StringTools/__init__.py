from .nodes import StringConcat, StringReplace, StringSlice

NODE_CLASS_MAPPINGS = {
    "StringConcat": StringConcat,
    "StringReplace": StringReplace,
    "StringSlice": StringSlice,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringConcat": "String Concatenate",
    "StringReplace": "String Replace",
    "StringSlice": "String Slice",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
