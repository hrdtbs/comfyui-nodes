from .utils import AnyType

# Global storage for wireless data
WIRELESS_DATA = {}

class SimpleWirelessSend:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "data": (AnyType("*"),),
                "key": ("STRING", {"default": "my_data"}),
            },
        }

    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("data",)
    FUNCTION = "send"
    CATEGORY = "SimpleWireless"

    def send(self, data, key):
        global WIRELESS_DATA
        WIRELESS_DATA[key] = data
        return (data,)

class SimpleWirelessReceive:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key": ("STRING", {"default": "my_data"}),
            },
            "optional": {
                "trigger": (AnyType("*"),), # Used to force execution order if needed
            }
        }

    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("data",)
    FUNCTION = "receive"
    CATEGORY = "SimpleWireless"

    def receive(self, key, trigger=None):
        global WIRELESS_DATA
        if key in WIRELESS_DATA:
            return (WIRELESS_DATA[key],)
        else:
            print(f"SimpleWireless: Key '{key}' not found in storage.")
            return (None,)
