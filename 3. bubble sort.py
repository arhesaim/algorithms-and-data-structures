import numpy as np

nums = list(np.random.randint(0, 9, 15))
j = 1

print(nums)

for k in range(len(nums)):
    for i in range(len(nums) - j):
        if nums[i] > nums[i+1]:
            nums[i+1], nums[i] = nums[i], nums[i+1]
    j += 1

print(nums)