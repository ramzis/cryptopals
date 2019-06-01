#!/usr/bin/python3
import unittest
import string
from c2 import cycle_xor


class TestChallenge(unittest.TestCase):

    def test_single_byte_xor_cypher(self):
        data = 'The quick brown fox jumps over the lazy dog'
        z = data.encode()
        keys = range(256)
        for key in keys:
            e = cycle_xor(z, bytes([key]))
            # print("Encoded", key, e)
            d = single_byte_xor_cypher(e)[0][0]
            # print("Decoded", d.decode())
            self.assertEqual(data, d.decode())

        message = single_byte_xor_cypher(
            bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))[0][0]
        print(message.decode())


def single_byte_xor_cypher(byte_text):
    rs = []
    for key in range(256):
        m = cycle_xor(byte_text, bytes([key]))
        rs.append((m, bhattacharyya_coeff(m), bytes([key])))
    return sorted(rs, key=lambda r: r[1], reverse=True)


def chi_squared_coeff(text):

    from collections import Counter, defaultdict

    def valid(byte):
        return byte in string.ascii_letters.encode() + b' \'\".,;?!'

    if not all(map(valid, text)):
        return 10e+10

    text_length = len(text)

    english_freqs_including_space = [
        0.0651738, 0.0124248, 0.0217339, 0.0349835,  # 'A', 'B', 'C', 'D',..., ' '
        0.1041442, 0.0197881, 0.0158610, 0.0492888,
        0.0558094, 0.0009033, 0.0050529, 0.0331490,
        0.0202124, 0.0564513, 0.0596302, 0.0137645,
        0.0008606, 0.0497563, 0.0515760, 0.0729357,
        0.0225134, 0.0082903, 0.0171272, 0.0013692,
        0.0145984, 0.0007836, 0.1918182
    ]

    expected_count = defaultdict(int, {ord(letter): freq * text_length for (letter, freq) in zip(
        list(string.ascii_lowercase) + [' '], english_freqs_including_space)})

    actual_count = Counter(text.lower())

    score = 0
    for letter in actual_count.keys():
        score += (actual_count[letter] - expected_count[letter]) ** 2 / (
            expected_count[letter] or 1)

    return score


def bhattacharyya_coeff(text):

    from collections import Counter, defaultdict
    from math import sqrt

    text_length = len(text)

    english_freqs_including_space = [
        0.0651738, 0.0124248, 0.0217339, 0.0349835,  # 'A', 'B', 'C', 'D',..., ' '
        0.1041442, 0.0197881, 0.0158610, 0.0492888,
        0.0558094, 0.0009033, 0.0050529, 0.0331490,
        0.0202124, 0.0564513, 0.0596302, 0.0137645,
        0.0008606, 0.0497563, 0.0515760, 0.0729357,
        0.0225134, 0.0082903, 0.0171272, 0.0013692,
        0.0145984, 0.0007836, 0.1918182
    ]

    expected_count = defaultdict(int, {ord(letter): freq * text_length for (letter, freq) in zip(
        list(string.ascii_lowercase) + [' '], english_freqs_including_space)})

    actual_count = Counter(text.lower())

    score = 0
    for letter in actual_count.keys():
        score += sqrt(actual_count[letter] * expected_count[letter])

    return score


def etaoin_coeff(text):

    from collections import Counter, defaultdict

    english_freqs_including_space = [
        0.0651738, 0.0124248, 0.0217339, 0.0349835,  # 'A', 'B', 'C', 'D',..., ' '
        0.1041442, 0.0197881, 0.0158610, 0.0492888,
        0.0558094, 0.0009033, 0.0050529, 0.0331490,
        0.0202124, 0.0564513, 0.0596302, 0.0137645,
        0.0008606, 0.0497563, 0.0515760, 0.0729357,
        0.0225134, 0.0082903, 0.0171272, 0.0013692,
        0.0145984, 0.0007836, 0.1918182
    ]

    values = defaultdict(int, {ord(letter): freq for(letter, freq) in zip(
        list(string.ascii_lowercase) + [' '], english_freqs_including_space)})

    counts = Counter(text.lower())

    score = 0
    for letter in counts.keys():
        score += values[letter] * counts[letter]

    return score


if __name__ == '__main__':
    unittest.main()
