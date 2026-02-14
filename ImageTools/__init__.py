from .nodes import ImageProperties, ImageResizeCalculator

NODE_CLASS_MAPPINGS = {
    "ImageProperties": ImageProperties,
    "ImageResizeCalculator": ImageResizeCalculator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageProperties": "Image Properties",
    "ImageResizeCalculator": "Image Resize Calculator",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
