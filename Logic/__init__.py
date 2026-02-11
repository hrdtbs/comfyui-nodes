from .nodes import LogicBoolean, LogicNot, LogicOperation, LogicCompare

NODE_CLASS_MAPPINGS = {
    "LogicBoolean": LogicBoolean,
    "LogicNot": LogicNot,
    "LogicOperation": LogicOperation,
    "LogicCompare": LogicCompare,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LogicBoolean": "Logic Boolean",
    "LogicNot": "Logic Not",
    "LogicOperation": "Logic Operation",
    "LogicCompare": "Logic Compare",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
