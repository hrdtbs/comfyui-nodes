class AnyType(str):
    """
    A special type that compares equal to any other type.
    This is used to accept any input in ComfyUI nodes.
    """
    def __ne__(self, __value: object) -> bool:
        return False

    def __eq__(self, __value: object) -> bool:
        return True

    def __str__(self) -> str:
        return self
