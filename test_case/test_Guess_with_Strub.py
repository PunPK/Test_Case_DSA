import unittest
from unittest.mock import patch
from programs.Guess import guess_int, guess_float


class TestGuessFunctions(unittest.TestCase):

    @patch("programs.Guess.randint")
    def test_guess_int(self, mock_randint):
        mock_randint.return_value = 5

        result = guess_int(1, 10)

        self.assertEqual(result, 5)
        mock_randint.assert_called_once_with(1, 10)

    @patch("programs.Guess.uniform")
    def test_guess_float(self, mock_uniform):
        mock_uniform.return_value = 5.5

        result = guess_float(1.0, 10.0)

        self.assertEqual(result, 5.5)
        mock_uniform.assert_called_once_with(1.0, 10.0)
