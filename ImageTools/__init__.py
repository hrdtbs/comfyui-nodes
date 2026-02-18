from .nodes import ImageProperties, ImageResizeCalculator, ImageScaleToTotalPixels

NODE_CLASS_MAPPINGS = {
    "ImageProperties": ImageProperties,
    "ImageResizeCalculator": ImageResizeCalculator,
    "ImageScaleToTotalPixels": ImageScaleToTotalPixels,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageProperties": "Image Properties",
    "ImageResizeCalculator": "Image Resize Calculator",
    "ImageScaleToTotalPixels": "Image Scale to Megapixels",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
