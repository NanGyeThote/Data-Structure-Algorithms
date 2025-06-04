# Test Binary Search

import unittest
from BinarySearch import Binary_Search

class TestBinarySearch(unittest.TestCase):
    def test_target_found(self):
        self.assertEqual(Binary_Search([1, 2, 3, 4, 5], 3), 2)

    def test_target_not_found(self):
        self.assertEqual(Binary_Search([1, 2, 3, 4, 5], 6), -1)

    def test_empty_list(self):
        self.assertEqual(Binary_Search([], 1), -1)

    def test_single_element_found(self):
        self.assertEqual(Binary_Search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(Binary_Search([5], 3), -1)

    def test_duplicates(self):
        self.assertIn(Binary_Search([1, 2, 2, 2, 3], 2), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()