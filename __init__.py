import importlib
import os
import sys

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# List of folders to ignore
IGNORE_FOLDERS = {'__pycache__', '.git', 'tests'}

# Get current directory
current_dir = os.path.dirname(__file__)

# Iterate over subdirectories
for item in os.listdir(current_dir):
    item_path = os.path.join(current_dir, item)
    if os.path.isdir(item_path) and item not in IGNORE_FOLDERS:
        # check if it has __init__.py
        if '__init__.py' in os.listdir(item_path):
            try:
                # Try relative import (for package usage)
                module = importlib.import_module(f".{item}", package=__name__)
            except ImportError:
                 # Try absolute import (for local testing/script usage)
                 try:
                    module = importlib.import_module(item)
                 except ImportError as e:
                    print(f"Failed to load module {item}: {e}")
                    continue

            if hasattr(module, "NODE_CLASS_MAPPINGS"):
                NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
            if hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS"):
                NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
