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


class LogicBoolean:
    """
    A node that outputs a constant boolean value.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "value": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_value"
    CATEGORY = "h2nodes/Logic"

    def get_value(self, value: bool) -> tuple[bool]:
        return (value,)


class LogicNot:
    """
    A node that inverts a boolean value.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "value": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "invert"
    CATEGORY = "h2nodes/Logic"

    def invert(self, value: bool) -> tuple[bool]:
        return (not value,)


class LogicOperation:
    """
    A node that performs boolean logic operations.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "op": (["AND", "OR", "XOR", "NAND", "NOR", "XNOR"], {"default": "AND"}),
                "a": ("BOOLEAN", {"default": True}),
                "b": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "operate"
    CATEGORY = "h2nodes/Logic"

    def operate(self, op: str, a: bool, b: bool) -> tuple[bool]:
        if op == "AND":
            return (a and b,)
        elif op == "OR":
            return (a or b,)
        elif op == "XOR":
            return (a != b,)
        elif op == "NAND":
            return (not (a and b),)
        elif op == "NOR":
            return (not (a or b),)
        elif op == "XNOR":
            return (a == b,)
        return (False,)


class LogicCompare:
    """
    A node that compares two inputs of any type.
    """
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "op": (["==", "!=", "<", ">", "<=", ">="], {"default": "=="}),
                "a": (AnyType("*"),),
                "b": (AnyType("*"),),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "compare"
    CATEGORY = "h2nodes/Logic"

    def compare(self, op: str, a, b) -> tuple[bool]:
        try:
            if op == "==":
                return (a == b,)
            elif op == "!=":
                return (a != b,)
            elif op == "<":
                return (a < b,)
            elif op == ">":
                return (a > b,)
            elif op == "<=":
                return (a <= b,)
            elif op == ">=":
                return (a >= b,)
        except Exception:
            return (False,)
        return (False,)
