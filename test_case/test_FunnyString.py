from programs.FunnyString import funnyString
import unittest


class TestFunnyString(unittest.TestCase):

    def test_funny(self):

        self.assertEqual(funnyString("acxz"), "Funny")

    def test_not_funny(self):

        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_single_char(self):

        self.assertEqual(funnyString("a"), "Funny")

    def test_odd_length_and_funny(self):

        self.assertEqual(funnyString("abcdedcba"), "Funny")

    def test_even_length_and_funny(self):

        self.assertEqual(funnyString("abcdeedcba"), "Funny")

    def test_odd_length_and_not_funny(self):

        self.assertEqual(funnyString("abcdeicba"), "Not Funny")

    def test_even_length_and_not_funny(self):

        self.assertEqual(funnyString("abcqdefedcba"), "Not Funny")
