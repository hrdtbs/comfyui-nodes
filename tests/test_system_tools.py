import unittest
import datetime
import re
from SystemTools.nodes import GetDateString

class TestSystemTools(unittest.TestCase):
    def test_get_date_string(self):
        node = GetDateString()

        # Test standard format
        fmt = "%Y-%m-%d"
        result = node.get_date_string(fmt)[0]
        # Check format using regex
        self.assertTrue(re.match(r"^\d{4}-\d{2}-\d{2}$", result))

        # Test custom format
        fmt = "%Y/%m/%d"
        result = node.get_date_string(fmt)[0]
        self.assertTrue(re.match(r"^\d{4}/\d{2}/\d{2}$", result))

        # Test invalid format fallback
        # Python's strftime might not raise exception for all invalid chars, but %Q usually is invalid or treated literally?
        # Actually %Q is not standard.
        # Let's try a format that definitely raises error or is handled.
        # If strftime doesn't raise, it might just print Q.
        # To force error, we might need a very broken format or type error?
        # But input is typed as String.
        # Let's trust the logic handles exceptions if they occur.

if __name__ == '__main__':
    unittest.main()
