from programs.Grid_Challenge import gridChallenge
import unittest


class TestGridChallenge(unittest.TestCase):

    def test_true_grid(self):

        result = gridChallenge(["ebacd", "fghij", "olmnp"])
        self.assertEqual(result, "YES")

    def test_false_grid(self):

        result = gridChallenge(["ebacd", "fghij", "olmnz"])
        self.assertEqual(result, "YES")

    def test_single_row(self):

        result = gridChallenge(["abcd"])
        self.assertEqual(result, "YES")

    def test_single_column(self):

        result = gridChallenge(["e", "f", "g", "h"])
        self.assertEqual(result, "YES")

    def test_empty_grid(self):

        result = gridChallenge([""])
        self.assertEqual(result, "YES")

    def test_small_grid_true(self):

        result = gridChallenge(["abc", "def", "ghi"])
        self.assertEqual(result, "YES")

    def test_small_grid_false(self):

        result = gridChallenge(["abc", "dec", "ghi"])
        self.assertEqual(result, "YES")

    def test_alternation_characters_unsorted(self):
        result = gridChallenge(["aab", "bba", "aab"])
        self.assertEqual(result, "NO")
