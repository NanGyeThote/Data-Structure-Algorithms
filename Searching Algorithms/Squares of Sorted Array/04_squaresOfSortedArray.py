# Test Squares of Sorted Array

import unittest
from SquaresOfSortedArray import sortedSquares

def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return sorted(nums)

class TestSortedSquares(unittest.TestCase):
    def test_mixed(self):
        self.assertEqual(sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    def test_negative_positive(self):
        self.assertEqual(sortedSquares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])

    def test_single_element(self):
        self.assertEqual(sortedSquares([1]), [1])

    def test_empty(self):
        self.assertEqual(sortedSquares([]), [])

    def test_all_negative(self):
        self.assertEqual(sortedSquares([-2, -1]), [1, 4])

if __name__ == "__main__":
    unittest.main()
