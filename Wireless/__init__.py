from .nodes import WirelessSend, WirelessReceive

NODE_CLASS_MAPPINGS = {
    "WirelessSend": WirelessSend,
    "WirelessReceive": WirelessReceive
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WirelessSend": "Wireless Send",
    "WirelessReceive": "Wireless Receive"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
