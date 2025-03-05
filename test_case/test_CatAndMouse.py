from programs.CatAndMouse import catAndMouse
import unittest


class TestCatAndMouse(unittest.TestCase):

    def test_cat_and_mouse_equal_distance(self):

        result = catAndMouse(1, 3, 2)
        self.assertEqual(result, "Mouse C")

    def test_cat_and_mouse_equal_distance_2(self):

        result = catAndMouse(3, 1, 2)
        self.assertEqual(result, "Mouse C")

    def test_cat_a_closer(self):

        result = catAndMouse(1, 4, 2)
        self.assertEqual(result, "Cat A")

    def test_cat_b_closer(self):

        result = catAndMouse(4, 1, 2)
        self.assertEqual(result, "Cat B")

    def test_cat_a_at_mouse(self):

        result = catAndMouse(2, 5, 2)
        self.assertEqual(result, "Cat A")

    def test_cat_b_at_mouse(self):

        result = catAndMouse(5, 2, 2)
        self.assertEqual(result, "Cat B")
