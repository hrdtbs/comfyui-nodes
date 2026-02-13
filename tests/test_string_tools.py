import unittest
from StringTools.nodes import StringConcat, StringReplace, StringSlice, StringRegexReplace, StringSplit

class TestStringTools(unittest.TestCase):
    def test_string_concat(self):
        node = StringConcat()
        # Test basic concatenation
        self.assertEqual(node.concatenate("Hello", "World", " "), ("Hello World",))
        # Test with empty separator
        self.assertEqual(node.concatenate("A", "B", ""), ("AB",))
        # Test with empty strings
        self.assertEqual(node.concatenate("", "World", "-"), ("-World",))

    def test_string_replace(self):
        node = StringReplace()
        # Test basic replacement
        self.assertEqual(node.replace("Hello World", "World", "ComfyUI"), ("Hello ComfyUI",))
        # Test no match
        self.assertEqual(node.replace("Hello World", "Foo", "Bar"), ("Hello World",))
        # Test empty replacement
        self.assertEqual(node.replace("Hello World", " ", ""), ("HelloWorld",))

    def test_string_slice(self):
        node = StringSlice()
        text = "Hello World"

        # Test default (0, 0 -> full string)
        self.assertEqual(node.slice_string(text, 0, 0), ("Hello World",))

        # Test explicit slice
        self.assertEqual(node.slice_string(text, 0, 5), ("Hello",))

        # Test middle slice
        self.assertEqual(node.slice_string(text, 6, 11), ("World",))

        # Test start only (end=0 -> None)
        self.assertEqual(node.slice_string(text, 6, 0), ("World",))

        # Test negative indices
        self.assertEqual(node.slice_string(text, -5, 0), ("World",))
        self.assertEqual(node.slice_string(text, 0, -6), ("Hello",))

    def test_string_regex_replace(self):
        node = StringRegexReplace()
        # Basic replacement
        self.assertEqual(node.regex_replace("Hello World", "World", "ComfyUI"), ("Hello ComfyUI",))
        # Regex pattern
        self.assertEqual(node.regex_replace("Hello 123", r"\d+", "Numbers"), ("Hello Numbers",))
        # Backreferences
        self.assertEqual(node.regex_replace("Hello World", r"(\w+) (\w+)", r"\2 \1"), ("World Hello",))
        # Invalid regex (should return original)
        # Note: Depending on implementation, this might print an error but return original string
        self.assertEqual(node.regex_replace("Hello", "[", "Fail"), ("Hello",))

    def test_string_split(self):
        node = StringSplit()
        # Basic split
        self.assertEqual(node.split_string("A,B,C", ","), (["A", "B", "C"],))
        # Split by whitespace (empty separator)
        self.assertEqual(node.split_string("A B C", ""), (["A", "B", "C"],))
        # No separator match
        self.assertEqual(node.split_string("ABC", ","), (["ABC"],))

if __name__ == '__main__':
    unittest.main()
