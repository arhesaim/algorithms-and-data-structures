import random
import time

# Generate a list of 500 random integers between 0 and 999
lst = [random.randint(0, 999) for i in range(500)]

def selection_sort(lst):
    n = len(lst)
    count = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            count += 1
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        count += 1
    return lst, count

def merge_sort(lst):
    if len(lst) <= 1:
        return lst, 0
    mid = len(lst) // 2
    left, count_left = merge_sort(lst[:mid])
    right, count_right = merge_sort(lst[mid:])
    merged, count_merge = merge(left, right)
    return merged, count_left + count_right + count_merge

def merge(left, right):
    merged = []
    count = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        count += 1
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged, count

# Sort the list using Merge sort
sorted_lst_merge, count_merge = merge_sort(lst)
print("Merge sort count:", count_merge)

# Sort the list using Selection sort
sorted_lst_sel, count_sel = selection_sort(lst)
print("Selection sort count:", count_sel)

start_time = time.time()
sorted_lst_sel, count_sel = selection_sort(lst)
end_time = time.time()
print("Selection sort time:", end_time - start_time, "seconds")

start_time = time.time()
sorted_lst_merge, count_merge = merge_sort(lst)
end_time = time.time()
print("Merge sort time:", end_time - start_time, "seconds")