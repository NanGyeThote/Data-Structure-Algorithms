# Test Remove Element

import unittest
from RemoveElement import removeElement

class TestRemoveElement(unittest.TestCase):
    def test_case1(self):
        nums = [3, 2, 2, 3]
        val = 3
        k = removeElement(nums, val)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [2, 2])

    def test_case2(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        k = removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0, 0, 1, 3, 4])

    def test_empty(self):
        nums = []
        val = 1
        self.assertEqual(removeElement(nums, val), 0)

if __name__ == "__main__":
    unittest.main()