import sys
import os
import unittest

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Logic.nodes import LogicBoolean, LogicNot, LogicOperation, LogicCompare, LogicSwitch

class TestLogic(unittest.TestCase):
    def test_logic_boolean(self):
        node = LogicBoolean()
        self.assertEqual(node.get_value(True)[0], True)
        self.assertEqual(node.get_value(False)[0], False)

    def test_logic_not(self):
        node = LogicNot()
        self.assertEqual(node.invert(True)[0], False)
        self.assertEqual(node.invert(False)[0], True)

    def test_logic_operation(self):
        node = LogicOperation()
        # AND
        self.assertEqual(node.operate("AND", True, True)[0], True)
        self.assertEqual(node.operate("AND", True, False)[0], False)
        # OR
        self.assertEqual(node.operate("OR", True, False)[0], True)
        self.assertEqual(node.operate("OR", False, False)[0], False)
        # XOR
        self.assertEqual(node.operate("XOR", True, False)[0], True)
        self.assertEqual(node.operate("XOR", True, True)[0], False)
        # NAND
        self.assertEqual(node.operate("NAND", True, True)[0], False)
        self.assertEqual(node.operate("NAND", True, False)[0], True)
        # NOR
        self.assertEqual(node.operate("NOR", True, False)[0], False)
        self.assertEqual(node.operate("NOR", False, False)[0], True)
        # XNOR
        self.assertEqual(node.operate("XNOR", True, True)[0], True)
        self.assertEqual(node.operate("XNOR", True, False)[0], False)

    def test_logic_compare(self):
        node = LogicCompare()
        # Integers
        self.assertEqual(node.compare("==", 5, 5)[0], True)
        self.assertEqual(node.compare("!=", 5, 3)[0], True)
        self.assertEqual(node.compare(">", 5, 3)[0], True)
        self.assertEqual(node.compare("<", 3, 5)[0], True)
        self.assertEqual(node.compare(">=", 5, 5)[0], True)
        self.assertEqual(node.compare("<=", 3, 5)[0], True)

        # Strings
        self.assertEqual(node.compare("==", "hello", "hello")[0], True)
        self.assertEqual(node.compare("!=", "hello", "world")[0], True)

        # Mixed Types (handling exceptions)
        # String vs Int
        # In Python 3, 'hello' > 5 raises TypeError. The node should catch this and return False.
        self.assertEqual(node.compare(">", "hello", 5)[0], False)
        self.assertEqual(node.compare("<", "hello", 5)[0], False)

        # Equality between types usually works in Python (returns False)
        self.assertEqual(node.compare("==", "5", 5)[0], False)

    def test_logic_switch(self):
        node = LogicSwitch()
        # Boolean switch
        self.assertEqual(node.switch(True, "A", "B")[0], "A")
        self.assertEqual(node.switch(False, "A", "B")[0], "B")

        # Mixed types
        self.assertEqual(node.switch(True, 100, "String")[0], 100)
        self.assertEqual(node.switch(False, 100, "String")[0], "String")

        # None handling (if needed, though standard inputs aren't usually None in ComfyUI without custom nodes)
        self.assertEqual(node.switch(True, None, 1)[0], None)


if __name__ == '__main__':
    unittest.main()
