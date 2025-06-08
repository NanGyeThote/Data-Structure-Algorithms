# Remove Element

def removeElement(nums, val):
    if not nums:
        return 0
    count = 0
    for i in nums:
        if i != val:
            nums[count] = i
            count += 1

    return count