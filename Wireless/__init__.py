from .nodes import Wireless

NODE_CLASS_MAPPINGS = {
    "Wireless": Wireless,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Wireless": "Wireless",
}

WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
