#!/usr/bin/python3
import unittest
import string
from c2 import cycle_xor


class TestChallenge(unittest.TestCase):

    def test_single_byte_xor_cypher(self):
        data = "The sun is shining today"
        z = data.encode()
        keys = list(string.ascii_uppercase)
        for key in keys:
            e = cycle_xor(z, key.encode())
            d = single_byte_xor_cypher(e.hex())
            self.assertEqual(d, data)

        message = single_byte_xor_cypher(
            '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
        print(message)


def single_byte_xor_cypher(hex):
    b = bytes.fromhex(hex)
    keys = list(string.ascii_uppercase)
    rs = []
    for key in keys:
        m = cycle_xor(b, bytes(key, "UTF-8")).decode("UTF-8")
        rs.append((m, plaintext_score(m)))
    return max(rs, key=lambda r: r[1])[0]


def plaintext_score(text):
    ls = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u',
          'm', 'f', 'p', 'g', 'w', 'y', 'b', 'v', 'k', 'x', 'j', 'q', 'z']
    score = 0
    for c in text:
        try:
            score += 26 - ls.index(c.lower())
        except ValueError:
            pass
    return score


if __name__ == '__main__':
    unittest.main()
