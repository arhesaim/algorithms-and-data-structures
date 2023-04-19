import random


def radix_sort(arr):
    for i in range(3):  # Sort by each digit, from right to left
        buckets = [0] * 10
        output = [0] * len(arr)
        for num in arr:
            digit = (num // 10 ** i) % 10  # Extract the i-th digit from the right
            buckets[digit] += 1
        for j in range(1, 10):
            buckets[j] += buckets[j-1]
        for num in reversed(arr):
            digit = (num // 10 ** i) % 10
            output[buckets[digit] - 1] = num
            buckets[digit] -= 1
        arr = output
    return arr

arr = [random.randint(100, 999) for _ in range(50)]

print(radix_sort(arr))