#!/usr/bin/python3
import unittest


class TestChallenge(unittest.TestCase):

    def test_fixed_xor(self):
        data = bytes.fromhex('1c0111001f010100061a024b53535009181c')
        key = bytes.fromhex('686974207468652062756c6c277320657965')
        print(key.decode())
        xor = fixed_xor(data, key)
        xor = xor.hex()
        self.assertEqual(xor, '746865206b696420646f6e277420706c6179')

    def test_cycle_xor(self):
        data = bytes.fromhex('1c0111001f010100061a024b53535009181c')
        key = bytes.fromhex('686974207468652062756c6c277320657965')
        xor = cycle_xor(data, key)
        xor = xor.hex()
        self.assertEqual(xor, '746865206b696420646f6e277420706c6179')


def fixed_xor(data, key):
    # return ''.join(chr(x ^ y) for x, y in zip(data, key))
    return bytes([a ^ b for a, b in zip(data, key)])


def cycle_xor(data, key):
    from itertools import cycle
    return bytes([c ^ k for c, k in zip(data, cycle(key))])

if __name__ == '__main__':
    unittest.main()
