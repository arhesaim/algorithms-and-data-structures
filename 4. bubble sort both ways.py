import numpy as np

nums = list(np.random.randint(0, 9, 15))
j = 0
k = 1

print(nums)

for p in range(len(nums)):
    for i in range(k, len(nums) - j, 1):
        if nums[i-1] > nums[i]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
        if nums[-i] < nums[-i-1]:
            nums[-i], nums[-i-1] = nums[-i-1], nums[-i]
    j += 1
    k += 1

print(nums)