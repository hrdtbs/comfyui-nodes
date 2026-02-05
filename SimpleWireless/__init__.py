from .wireless import SimpleWirelessSend, SimpleWirelessReceive

NODE_CLASS_MAPPINGS = {
    "SimpleWirelessSend": SimpleWirelessSend,
    "SimpleWirelessReceive": SimpleWirelessReceive
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleWirelessSend": "Wireless Send",
    "SimpleWirelessReceive": "Wireless Receive"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
