from programs.Caesar_Cipher import caesarCipher
import unittest


class TestCaesarCipher(unittest.TestCase):

    def test_text_basic(self):

        result = caesarCipher("abc", 3)
        self.assertEqual(result, "def")

    def test_empty_string(self):

        result = caesarCipher("", 5)
        self.assertEqual(result, "")

    def test_non_alpha_characters(self):

        result = caesarCipher("abc!123", 2)
        self.assertEqual(result, "cde!123")

    def test_k_zero(self):

        result = caesarCipher("hello", 0)
        self.assertEqual(result, "hello")

    def test_large_k_value(self):

        result = caesarCipher("hello", 28)
        self.assertEqual(result, "jgnnq")

    def test_uppercase_characters(self):

        result = caesarCipher("HELLO", 3)
        self.assertEqual(result, "KHOOR")

    def test_mixed_case_string(self):

        result = caesarCipher("HeLLo WoRLd", 4)
        self.assertEqual(result, "LiPPs AsVPh")
