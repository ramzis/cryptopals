#!/usr/bin/python3
import unittest
import string
from c3 import single_byte_xor_cypher


class TestChallenge(unittest.TestCase):

    def test_detect_single_character_xor(self):
        input = './resources/{}.txt'.format('4')
        max_score = 0
        answer = None
        ds = []
        with open(input) as f:
            for line in f:
                e = bytes.fromhex(line.strip())
                d = single_byte_xor_cypher(e)
                ds += d
        answer = sorted(ds, key=lambda x: x[1], reverse=True)[0]
        print(answer[0].decode())

if __name__ == '__main__':
    unittest.main()
