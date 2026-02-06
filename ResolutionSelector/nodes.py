import re

class ResolutionSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "resolution": (
                    [
                        "SD1.5 - 512x512 (1:1)",
                        "SD1.5 - 768x512 (3:2)",
                        "SD1.5 - 512x768 (2:3)",
                        "SDXL / Illustrious - 1024x1024 (1:1)",
                        "SDXL / Illustrious - 1152x896 (9:7)",
                        "SDXL / Illustrious - 896x1152 (7:9)",
                        "SDXL / Illustrious - 1216x832 (19:13)",
                        "SDXL / Illustrious - 832x1216 (13:19)",
                        "SDXL / Illustrious - 1344x768 (7:4)",
                        "SDXL / Illustrious - 768x1344 (4:7)",
                        "SDXL / Illustrious - 1536x640 (12:5)",
                        "SDXL / Illustrious - 640x1536 (5:12)",
                    ],
                    {"default": "SDXL / Illustrious - 1024x1024 (1:1)"}
                )
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "select_resolution"
    CATEGORY = "h2nodes/Image"

    def select_resolution(self, resolution):
        try:
            match = re.search(r'(\d+)x(\d+)', resolution)
            if match:
                width = int(match.group(1))
                height = int(match.group(2))
                return (width, height)
            else:
                return (0, 0)
        except Exception:
             return (0, 0)
