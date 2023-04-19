import math
import random

def golden_section_search(arr, x):
    a = 0
    b = len(arr) - 1
    phi = (1 + math.sqrt(5)) / 2  # Golden ratio
    while True:
        d = int((b - a) / phi)
        i = a + d
        j = b - d
        if arr[i] == x:
            return i
        elif arr[j] == x:
            return j
        elif d == 0:
            return -1
        elif arr[i] < x:
            a = i
        else:
            b = i

arr = [2,3,4,5,6,7,8,12,67,89,670,767,924]
print(golden_section_search(arr, 767))