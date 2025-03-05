from programs.FizzBuzz import fizz_buzz
import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_give_3_is_fizz(self):
        list_number = [3]
        result = fizz_buzz(list_number)
        self.assertIn("Fizz", result)

    def test_give_5_is_buzz(self):
        list_number = [5]
        result = fizz_buzz(list_number)
        self.assertIn("Buzz", result)

    def test_give_15_is_fizzbuzz(self):
        list_number = [15]
        result = fizz_buzz(list_number)
        self.assertIn("FizzBuzz", result)

    def test_give_1_2_4_7_8_11_is_fizzbuzz(self):
        list_number = [1, 2, 4, 7, 8, 11]
        result = fizz_buzz(list_number)
        for x in result:
            self.assertIsNone(x)

    def test_give_15_30_60_90_is_fizzbuzz(self):
        list_number = [15, 30, 60, 90]
        result = fizz_buzz(list_number)
        for x in result:
            self.assertIn("FizzBuzz", x)
