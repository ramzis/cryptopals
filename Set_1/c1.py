#!/usr/bin/python3
import unittest
import codecs


class TestChallenge(unittest.TestCase):

    def test_convert_hex_to_base64(self):
        self.assertEqual(
            convert_hex_to_base64(
                "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d").decode('UTF-8').strip(),
            "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")


def convert_hex_to_base64(hex):
    # Convert string to hex
    hex = codecs.decode(hex, 'hex')
    # Encode as base64 (bytes)
    return codecs.encode(hex, 'base64')


if __name__ == '__main__':
    unittest.main()
