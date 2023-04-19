import random
import time
import matplotlib.pyplot as plt

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Generate a random array of integers between 1 and 10000.
arr = [random.randint(1, 10000) for _ in range(100000)]

# Perform binary search for different array sizes and measure the time taken.
sizes = [100, 200, 500, 1000, 2000, 5000, 10000]
times = []
for size in sizes:
    arr_subset = arr[:size]
    x = random.randint(1, 10000)
    start_time = time.time()
    binary_search(arr_subset, x)
    end_time = time.time()
    times.append(end_time - start_time)

# Plot the results.
plt.plot(sizes, times)
plt.xlabel('Array size')
plt.ylabel('Time (seconds)')
plt.title('Binary search performance')
plt.show()