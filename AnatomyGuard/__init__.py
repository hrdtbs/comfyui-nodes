from .nodes import AnatomyDetectionMesh, AnatomyLogicEvaluator, IterativeAnatomyRefiner

NODE_CLASS_MAPPINGS = {
    "AnatomyDetectionMesh": AnatomyDetectionMesh,
    "AnatomyLogicEvaluator": AnatomyLogicEvaluator,
    "IterativeAnatomyRefiner": IterativeAnatomyRefiner
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnatomyDetectionMesh": "Anatomy Detection & Mesh",
    "AnatomyLogicEvaluator": "Anatomy Logic Evaluator",
    "IterativeAnatomyRefiner": "Iterative Anatomy Refiner"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
