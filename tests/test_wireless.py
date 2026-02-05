import sys
import os
import unittest

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from SimpleWireless.wireless import SimpleWirelessSend, SimpleWirelessReceive, WIRELESS_DATA
from SimpleWireless.utils import AnyType

class TestSimpleWireless(unittest.TestCase):
    def setUp(self):
        # Clear data before each test
        WIRELESS_DATA.clear()

    def test_send_receive(self):
        sender = SimpleWirelessSend()
        receiver = SimpleWirelessReceive()

        test_data = "Hello World"
        key = "msg"

        # Send
        result_send = sender.send(test_data, key)
        self.assertEqual(result_send[0], test_data)
        self.assertIn(key, WIRELESS_DATA)
        self.assertEqual(WIRELESS_DATA[key], test_data)

        # Receive
        result_receive = receiver.receive(key)
        self.assertEqual(result_receive[0], test_data)

    def test_receive_missing(self):
        receiver = SimpleWirelessReceive()
        result = receiver.receive("non_existent")
        self.assertIsNone(result[0])

    def test_any_type(self):
        any_t = AnyType("*")
        self.assertTrue(any_t == "INT")
        self.assertTrue(any_t == "STRING")
        self.assertTrue(any_t == 123)
        self.assertFalse(any_t != "IMAGE")

if __name__ == '__main__':
    unittest.main()
