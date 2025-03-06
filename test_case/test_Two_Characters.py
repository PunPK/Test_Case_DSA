from programs.Two_Characters import alternate
import unittest


class TestAlternateFunction(unittest.TestCase):

    def test_example_case(self):

        result = alternate("beabeefeab")
        self.assertEqual(result, 5)

    def test_no_alternation(self):

        result = alternate("aaaa")
        self.assertEqual(result, 0)

    def test_alternation(self):

        result = alternate("abcd")
        self.assertEqual(result, 2)

    def test_long_alternation(self):

        result = alternate("abababab")
        self.assertEqual(result, 8)

    def test_single_char(self):

        result = alternate("a")
        self.assertEqual(result, 0)

    def test_two_char_alternation(self):

        result = alternate("abab")
        self.assertEqual(result, 4)

    def test_mixed_characters(self):

        result = alternate("abcabcabc")
        self.assertEqual(result, 6)

    def test_empty_string(self):

        result = alternate("")
        self.assertEqual(result, 0)
