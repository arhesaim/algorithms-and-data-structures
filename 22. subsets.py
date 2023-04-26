def partition_set(numbers):

    total_sum = sum(numbers)

    if total_sum % 2 != 0:
        return None

    target_sum = total_sum // 2

    numbers.sort(reverse=True)

    subset_a = []
    subset_b = []

    for number in numbers:
        if sum(subset_a) + number <= target_sum:
            subset_a.append(number)
        else:
            subset_b.append(number)

    if sum(subset_a) == target_sum:
        return subset_a, subset_b
    else:
        return None

numbers = [1, 2, 3, 4, 5, 6, 7]
result = partition_set(numbers)
if result:
    subset_a, subset_b = result
    print("Subset A:", subset_a)
    print("Subset B:", subset_b)
else:
    print("No solution found.")
