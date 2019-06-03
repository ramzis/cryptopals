#!/usr/bin/python3
import unittest
import string
import base64
from c2 import cycle_xor
from c3 import single_byte_xor_cypher, bhattacharyya_coeff


class TestChallenge(unittest.TestCase):

    def test_detect_single_character_xor(self):
        input = './resources/{}.txt'.format('6')
        cypher_text = ""
        with open(input) as f:
            for line in f:
                cypher_text += line.strip()
        answer = break_repeating_key_xor(base64.b64decode(cypher_text))
        print(answer)

    def test_edit_distance(self):
        self.assertEqual(edit_distance_byte_string(
            b"this is a test", b"wokka wokka!!!", normalize=False), 37)
        self.assertEqual(edit_distance_byte_string(
            b"this is a test", b"wokka wokka!!!", normalize=True), 37 / 14)


def edit_distance_byte_string(a, b, normalize=False):
    assert len(a) == len(b)
    d = sum([hamming_distance_binary_string(c1, c2, True)
             for (c1, c2) in zip(a, b)])
    return d / len(a) if normalize else d


def hamming_distance_binary_string(a, b, convertFromInt=False):
    # a, b formatted as '01010101'
    if convertFromInt:
        a = f'{a:08b}'
        b = f'{b:08b}'
    assert len(a) == len(b)
    return sum(c1 != c2 for c1, c2 in zip(a, b))


def break_repeating_key_xor(cypher_text):
    from itertools import combinations

    # Find the edit distance of the first 2 key_size length blocks
    # of the cypher_text for key_size values in the range [2-40]
    key_edit_dist_dict = {}
    for key_size in range(2, 41):

        bytes_to_check = [cypher_text[
            idx * key_size:(idx + 1) * key_size] for idx in range(10)]
        byte_combinations = list(combinations(bytes_to_check, 2))
        ds = [edit_distance_byte_string(b1, b2, True)
              for (b1, b2) in byte_combinations]
        d = sum(ds) / len(ds)

        # print("Keysize", key_size, "norm edit distance", d)

        key_edit_dist_dict[key_size] = d

    # Try 3 key_size values with the smallest edit distance
    potential_keys = []
    for key_size, _ in sorted(key_edit_dist_dict.items(), key=lambda kv: kv[1])[:3]:
        # Loop through each potential byte in the key
        key = b''
        for byte_idx in range(key_size):
            # print("Checking ", key_size, "byte", byte_idx)
            xor_bytes = cypher_text[byte_idx::key_size]
            key += single_byte_xor_cypher(xor_bytes)[0][2]

        potential_keys.append(key)

    # Attempt to decipher the ciphertexts using the potential keys
    potential_plaintexts = []
    for key in potential_keys:
        d = cycle_xor(cypher_text, key)
        score = bhattacharyya_coeff(d)
        potential_plaintexts.append(
            {"plaintext": d, "key": key, "score": score})

    # Select the plaintext with the highest score for English
    answer = sorted(potential_plaintexts, key=lambda r: r[
                    "score"], reverse=True)[0]

    print(answer["key"].decode())
    print(answer["plaintext"].decode())

if __name__ == '__main__':
    unittest.main()
