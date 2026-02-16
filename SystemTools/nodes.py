import datetime

class GetDateString:
    """
    Outputs the current date/time as a string with a customizable format.
    Default format: %Y-%m-%d
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "format": ("STRING", {"default": "%Y-%m-%d"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("date_string",)
    FUNCTION = "get_date_string"
    CATEGORY = "h2nodes/SystemTools"

    def get_date_string(self, format: str) -> tuple[str]:
        try:
            return (datetime.datetime.now().strftime(format),)
        except Exception as e:
            print(f"[GetDateString] Invalid format '{format}': {e}")
            return (datetime.datetime.now().strftime("%Y-%m-%d"),)
