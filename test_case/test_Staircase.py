from programs.Staircase import staircase
import unittest


class TestStaircase(unittest.TestCase):
    def test_staircase_2(self):

        n = 2
        display = "#"
        expected_output = " #\n##"
        result = staircase(n, display)

        self.assertEqual(result, expected_output)

    def test_staircase_4(self):

        n = 4
        display = "#"
        expected_output = "   #\n  ##\n ###\n####"
        result = staircase(n, display)
        self.assertEqual(result, expected_output)

    def test_staircase_invalid_input_lower(self):

        n = 0
        display = "#"
        result = staircase(n, display)
        self.assertFalse(result)

    def test_staircase_invalid_input_upper(self):

        n = 31
        display = "#"
        result = staircase(n, display)

        self.assertFalse(result)

    def test_staircase_equal_case_min(self):

        n = 1
        display = "#"
        expected_output = "#"
        result = staircase(n, display)

        self.assertEqual(result, expected_output)

    def test_staircase_equal_case_max(self):

        n = 30
        display = "#"
        expected_output = ""
        for i in range(1, n + 1):
            expected_output += " " * (n - i) + "#" * i + "\n"
        expected_output = expected_output.strip()
        result = staircase(n, display)

        self.assertEqual(result, expected_output)
