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
