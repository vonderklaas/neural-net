nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
#                      k (pretends to stay on unique element)
#                      i (loop through all the elements)
# k = 5
def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k

k = removeDuplicates(nums)

nums = nums[:k]
print('unique k', k)
print('nums', nums)
