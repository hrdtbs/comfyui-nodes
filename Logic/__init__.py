from .nodes import LogicBoolean, LogicNot, LogicOperation, LogicCompare, LogicSwitch

NODE_CLASS_MAPPINGS = {
    "LogicBoolean": LogicBoolean,
    "LogicNot": LogicNot,
    "LogicOperation": LogicOperation,
    "LogicCompare": LogicCompare,
    "LogicSwitch": LogicSwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LogicBoolean": "Logic Boolean",
    "LogicNot": "Logic Not",
    "LogicOperation": "Logic Operation",
    "LogicCompare": "Logic Compare",
    "LogicSwitch": "Logic Switch",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
