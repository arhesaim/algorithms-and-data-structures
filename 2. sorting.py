import numpy as np

nums = list(np.random.randint(0, 9, 15))
# j = 1

# print(nums)

# for k in range(len(nums)-1):
#     for i in range(len(nums) - j):
#         if nums[i] > nums[i+1]:
#             nums[i+1], nums[i] = nums[i], nums[i+1]
#     j += 1

# print(nums)

print(nums)
elemNum = 0

for i in range(len(nums)):
    index = 0
    max = nums[0]
    for j in range(len(nums)-elemNum):
        if nums[j] > max:
            max = nums[j]
            index = j
    nums[-1-elemNum], nums[index] = nums[index], nums[-1-elemNum]
    elemNum += 1
    
print(nums)