nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i, num in enumerate(reversed(nums)):
    print(num)

for num in range(len(nums) - 1, -1, -1):
    print(nums[num])
    