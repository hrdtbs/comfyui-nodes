from .nodes import MathAdd

NODE_CLASS_MAPPINGS = {
    "MathAdd": MathAdd
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MathAdd": "Math Add"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
