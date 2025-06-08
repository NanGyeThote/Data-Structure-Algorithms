# Test Search Insert Position

import unittest
from SearchInsertPosition import searchInsert

class TestSearchInsert(unittest.TestCase):
    def test_found(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 5), 2)

    def test_insert_middle(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 2), 1)

    def test_insert_end(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 7), 4)

    def test_insert_start(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 0), 0)

    def test_single_element(self):
        self.assertEqual(searchInsert([1], 0), 0)

if __name__ == "__main__":
    unittest.main()