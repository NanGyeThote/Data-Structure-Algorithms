# Squares of Sorted Array

def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
        nums = sorted(nums)

    return nums