import random
import timeit

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n<q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quickSort(s_nums) + e_nums + quickSort(m_nums)
    
def bubbleSort(nums):
    j = 1
    for k in range(len(nums)):
        for i in range(len(nums) - j):
            if nums[i] > nums[i+1]:
                nums[i+1], nums[i] = nums[i], nums[i+1]
        j += 1
    
def quickSortTime():
    mySetUp = '''
from __main__ import quickSort
from __main__ import nums'''
    testCode = '''quickSort(nums)'''
    print(timeit.timeit(setup=mySetUp, stmt=testCode, number=100000))


def bubbleSortTime():
    mySetUp = '''
from __main__ import bubbleSort
from __main__ import nums'''
    testCode = '''bubbleSort(nums)'''
    print(timeit.timeit(setup=mySetUp, stmt=testCode, number=100000))
    

nums = []
for i in range(40):
    num = random.randint(0, 20)
    nums.append(num)


if __name__ == "__main__":
    quickSortTime()
    bubbleSortTime()