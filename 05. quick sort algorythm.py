import random
import time
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Generate a random array of integers between 1 and 10000.
arr = [random.randint(1, 10000) for _ in range(1000)]

# Sort the array using quicksort for different array sizes and measure the time taken.
sizes = [100, 200, 500, 1000, 2000, 5000, 6000, 7000, 8000, 9000, 10000]
times = []
for size in sizes:
    arr_subset = arr[:size]
    start_time = time.time()
    quicksort(arr_subset)
    end_time = time.time()
    times.append(end_time - start_time)

# Plot the results.
plt.plot(sizes, times)
plt.xlabel('Array size')
plt.ylabel('Time (seconds)')
plt.title('Quicksort performance')
plt.show()