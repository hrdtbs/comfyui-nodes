from .Math import NODE_CLASS_MAPPINGS as Math_MAPPINGS
from .Math import NODE_DISPLAY_NAME_MAPPINGS as Math_DISPLAY_MAPPINGS
from .Wireless import NODE_CLASS_MAPPINGS as Wireless_MAPPINGS
from .Wireless import NODE_DISPLAY_NAME_MAPPINGS as Wireless_DISPLAY_MAPPINGS
from .ResolutionSelector import NODE_CLASS_MAPPINGS as ResolutionSelector_MAPPINGS
from .ResolutionSelector import NODE_DISPLAY_NAME_MAPPINGS as ResolutionSelector_DISPLAY_MAPPINGS
from .AnatomyGuard import NODE_CLASS_MAPPINGS as AnatomyGuard_MAPPINGS
from .AnatomyGuard import NODE_DISPLAY_NAME_MAPPINGS as AnatomyGuard_DISPLAY_MAPPINGS

NODE_CLASS_MAPPINGS = {
    **Math_MAPPINGS,
    **Wireless_MAPPINGS,
    **ResolutionSelector_MAPPINGS,
    **AnatomyGuard_MAPPINGS,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **Math_DISPLAY_MAPPINGS,
    **Wireless_DISPLAY_MAPPINGS,
    **ResolutionSelector_DISPLAY_MAPPINGS,
    **AnatomyGuard_DISPLAY_MAPPINGS,
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
