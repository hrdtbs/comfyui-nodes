import sys
import os
import unittest

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Wireless.nodes import WirelessSend, WirelessReceive, WIRELESS_DATA
from Wireless.utils import AnyType

class TestWireless(unittest.TestCase):
    def setUp(self):
        # Clear data before each test
        WIRELESS_DATA.clear()

    def test_send_receive(self):
        sender = WirelessSend()
        receiver = WirelessReceive()

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
        receiver = WirelessReceive()
        result = receiver.receive("non_existent")
        self.assertIsNone(result[0])

    def test_any_type(self):
        any_t = AnyType("*")
        self.assertTrue(any_t == "INT")
        self.assertTrue(any_t == "STRING")
        self.assertTrue(any_t == 123)
        self.assertFalse(any_t != "IMAGE")
        self.assertEqual(str(any_t), "*")

    def test_input_types(self):
        # Send
        input_types_send = WirelessSend.INPUT_TYPES()
        self.assertIn("required", input_types_send)
        self.assertIn("data", input_types_send["required"])
        self.assertIn("key", input_types_send["required"])

        # Receive
        input_types_recv = WirelessReceive.INPUT_TYPES()
        self.assertIn("required", input_types_recv)
        self.assertIn("key", input_types_recv["required"])
        self.assertIn("optional", input_types_recv)
        self.assertIn("trigger", input_types_recv["optional"])

if __name__ == '__main__':
    unittest.main()
