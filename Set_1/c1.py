#!/usr/bin/python3
import unittest
import base64


class TestChallenge(unittest.TestCase):

    def test_convert_hex_to_base64(self):
        self.assertEqual(
            convert_hex_to_base64(
                "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"),
            "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")


def convert_hex_to_base64(hex):
    byte_string = bytes.fromhex(hex)
    print(byte_string.decode())
    return base64.b64encode(byte_string).decode()


if __name__ == '__main__':
    unittest.main()
