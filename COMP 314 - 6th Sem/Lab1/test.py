import unittest

from search import binary_search, linear_search


class SearchTestCase(unittest.TestCase):
    """Test cases for Search"""

    def test_linear_search(self):
        """unittest for linear search"""

        values = [5, 4, 9, 8, 11, 2, 6]
        self.assertEqual(linear_search(values, 9), 2)
        self.assertEqual(linear_search(values, 11), 4)
        self.assertEqual(linear_search(values, 6), 6)
        self.assertEqual(linear_search(values, 100), -1)

    def test_binary_search(self):
        """unittest for linear search"""

        values = [2, 4, 5, 6, 8, 9, 11]
        self.assertEqual(binary_search(values, 9), 5)
        self.assertEqual(binary_search(values, 11), 6)
        self.assertEqual(binary_search(values, 6), 3)
        self.assertEqual(binary_search(values, 100), -1)


if __name__ == "__main__":
    unittest.main()
