from programs.Alternating_Characters import alternatingCharacters
import unittest


class TestAlternatingCharacters(unittest.TestCase):

    def test_same_characters_5(self):

        result = alternatingCharacters("AAAAA")
        self.assertEqual(result, 4)

    def test_same_characters_3(self):

        result = alternatingCharacters("AAA")
        self.assertEqual(result, 2)

    def test_switch_string(self):

        result = alternatingCharacters("ABABAB")
        self.assertEqual(result, 0)

    def test_switch_string_2(self):

        result = alternatingCharacters("BABABABA")
        self.assertEqual(result, 0)

    def test_double_strings(self):

        result = alternatingCharacters("AABBAA")
        self.assertEqual(result, 3)

    def test_triple_string(self):

        result = alternatingCharacters("AAABBB")
        self.assertEqual(result, 4)

    def test_with_one_double_string_center(self):

        result = alternatingCharacters("ABBA")
        self.assertEqual(result, 1)

    def test_with_one_triple_string_center(self):

        result = alternatingCharacters("ABBBA")
        self.assertEqual(result, 2)
