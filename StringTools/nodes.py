import re

class StringConcat:
    """
    Concatenates two strings with a separator.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "text_a": ("STRING", {"multiline": True, "default": ""}),
                "text_b": ("STRING", {"multiline": True, "default": ""}),
                "separator": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "concatenate"
    CATEGORY = "h2nodes/StringTools"

    def concatenate(self, text_a: str, text_b: str, separator: str) -> tuple[str]:
        return (f"{text_a}{separator}{text_b}",)


class StringReplace:
    """
    Replaces occurrences of a substring in a string.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "old": ("STRING", {"default": ""}),
                "new": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "replace"
    CATEGORY = "h2nodes/StringTools"

    def replace(self, text: str, old: str, new: str) -> tuple[str]:
        return (text.replace(old, new),)


class StringSlice:
    """
    Slices a string given start and end indices.
    If end is 0, it slices to the end of the string.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "start": ("INT", {"default": 0, "min": -10000, "max": 10000}),
                "end": ("INT", {"default": 0, "min": -10000, "max": 10000}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "slice_string"
    CATEGORY = "h2nodes/StringTools"

    def slice_string(self, text: str, start: int, end: int) -> tuple[str]:
        # If end is 0, slice to the end.
        slice_end = None if end == 0 else end
        return (text[start:slice_end],)


class StringRegexReplace:
    """
    Replaces occurrences of a regex pattern in a string.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "pattern": ("STRING", {"default": "", "multiline": False}),
                "replacement": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "regex_replace"
    CATEGORY = "h2nodes/StringTools"

    def regex_replace(self, text: str, pattern: str, replacement: str) -> tuple[str]:
        try:
            return (re.sub(pattern, replacement, text),)
        except re.error as e:
            print(f"[StringRegexReplace] Invalid regex pattern '{pattern}': {e}")
            return (text,)


class StringSplit:
    """
    Splits a string. Can split by newline or by a separator.
    Returns a list of strings.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "separator": ("STRING", {"default": ","}),
                "split_mode": (["newline", "separator"], {"default": "newline"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("strings",)
    FUNCTION = "split_string"
    CATEGORY = "h2nodes/StringTools"

    def split_string(self, text: str, separator: str, split_mode: str = "separator") -> tuple[list[str]]:
        if split_mode == "newline":
            return ([line for line in text.splitlines() if line],)

        if not separator:
            return (text.split(),)
        return (text.split(separator),)


class StringJoin:
    """
    Joins a list of strings with a separator.
    Receives a list (batch) of strings and returns a single concatenated string.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "strings": ("STRING", {"forceInput": True}),
                "separator": ("STRING", {"default": "\\n", "multiline": False}),
            }
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "join_strings"
    CATEGORY = "h2nodes/StringTools"

    def join_strings(self, strings: list[str], separator: list[str]) -> tuple[str]:
        # Since INPUT_IS_LIST is True, 'separator' will be a list even if it's a single widget value.
        # We take the first element if it's a list.
        sep = separator[0] if isinstance(separator, list) and separator else "\n"

        # Handle literal "\n" string as newline character if user types "\n" in widget
        if sep == "\\n":
            sep = "\n"

        return (sep.join(strings),)

class StringCase:
    """
    Converts a string to a specified case (upper, lower, title, capitalize, swapcase).
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "case_method": (["upper", "lower", "title", "capitalize", "swapcase"], {"default": "upper"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "convert_case"
    CATEGORY = "h2nodes/StringTools"

    def convert_case(self, text: str, case_method: str) -> tuple[str]:
        if case_method == "upper":
            return (text.upper(),)
        if case_method == "lower":
            return (text.lower(),)
        if case_method == "title":
            return (text.title(),)
        if case_method == "capitalize":
            return (text.capitalize(),)
        if case_method == "swapcase":
            return (text.swapcase(),)
        return (text,)
