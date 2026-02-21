import unittest
from ListTools.nodes import ListGetItem, ListLength

class TestListTools(unittest.TestCase):
    def test_list_get_item(self):
        node = ListGetItem()
        my_list = ["a", "b", "c"]

        # Test valid index (passed as list due to INPUT_IS_LIST=True behavior)
        result = node.get_item(my_list, [1])
        self.assertEqual(result[0], "b")

        # Test index out of range
        result = node.get_item(my_list, [10])
        self.assertIsNone(result[0])

        # Test negative index
        result = node.get_item(my_list, [-1])
        self.assertEqual(result[0], "c")

    def test_list_length(self):
        node = ListLength()
        my_list = ["a", "b", "c"]

        # INPUT_IS_LIST=True means the first argument is the list itself
        result = node.get_length(my_list)
        self.assertEqual(result[0], 3)

        empty_list = []
        result = node.get_length(empty_list)
        self.assertEqual(result[0], 0)

if __name__ == '__main__':
    unittest.main()
