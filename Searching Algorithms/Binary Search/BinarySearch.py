# Binary Search Algorithms 

def Binary_Search(nums, target):
    left = 0 # starting index
    right = len(nums) - 1 # Ending index

    while left <= right:
        mid = (left + right) // 2 # To get the middle value
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

