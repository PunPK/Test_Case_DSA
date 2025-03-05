from programs.number_utils import is_prime_list
import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_2_3_is_prime(self):
        prime_list = [2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_6_8_is_not_prime(self):
        prime_list = [4, 6, 8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_1_is_not_prime(self):
        prime_list = [1]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_5_6_7_8_is_not_list_prime(self):
        prime_list = [5, 6, 7, 8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_11_13_17_19_is_not_list_prime(self):
        prime_list = [11, 13, 17, 19]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
