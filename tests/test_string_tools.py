import unittest
from StringTools.nodes import StringConcat, StringReplace, StringSlice, StringRegexReplace, StringSplit, StringJoin

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

        # Test default newline splitting
        text = "Line1\nLine2\r\nLine3\n\nLine4"
        # Expect empty line removed (Line3\n\nLine4 -> skip middle empty line)
        self.assertEqual(node.split_string(text, ",", "newline"), (["Line1", "Line2", "Line3", "Line4"],))

        # Test separator splitting
        self.assertEqual(node.split_string("A,B,C", ",", "separator"), (["A", "B", "C"],))

        # Test separator splitting with whitespace (empty separator)
        self.assertEqual(node.split_string("A B C", "", "separator"), (["A", "B", "C"],))

        # Test mixed newlines and separator behavior (should split by newline if mode is newline)
        self.assertEqual(node.split_string("A,B\nC,D", ",", "newline"), (["A,B", "C,D"],))

        # Test backward compatibility (no split_mode passed, defaults to separator)
        # This simulates an old workflow execution
        self.assertEqual(node.split_string("A,B,C", ","), (["A", "B", "C"],))

    def test_string_join(self):
        node = StringJoin()

        # Test basic join with default separator (simulated list input)
        # In ComfyUI with INPUT_IS_LIST=True, arguments are passed as lists.
        # strings input is a list of strings. separator is a list containing the widget value.
        self.assertEqual(node.join_strings(["A", "B", "C"], ["\n"]), ("A\nB\nC",))

        # Test join with comma
        self.assertEqual(node.join_strings(["A", "B", "C"], [","]), ("A,B,C",))

        # Test join with literal "\n" string handling
        self.assertEqual(node.join_strings(["A", "B"], ["\\n"]), ("A\nB",))

        # Test empty list
        self.assertEqual(node.join_strings([], ["\n"]), ("",))

        # Test single item
        self.assertEqual(node.join_strings(["Single"], ["\n"]), ("Single",))

if __name__ == '__main__':
    unittest.main()
