from .nodes import StringConcat, StringReplace, StringSlice, StringRegexReplace, StringSplit, StringJoin, StringCase

NODE_CLASS_MAPPINGS = {
    "StringConcat": StringConcat,
    "StringReplace": StringReplace,
    "StringSlice": StringSlice,
    "StringRegexReplace": StringRegexReplace,
    "StringSplit": StringSplit,
    "StringJoin": StringJoin,
    "StringCase": StringCase,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringConcat": "String Concatenate",
    "StringReplace": "String Replace",
    "StringSlice": "String Slice",
    "StringRegexReplace": "String Regex Replace",
    "StringSplit": "String Split",
    "StringJoin": "String Join",
    "StringCase": "String Case",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
