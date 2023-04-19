import time

# Create a dictionary with 1000000 elements
d = {i: i for i in range(1000000)}

# Create a list with 1000000 elements
lst = list(range(1000000))

# Measure the time taken to delete 100000 elements from the dictionary
start_time = time.time()
for i in range(100000):
    del d[i]
end_time = time.time()
dict_del_time = end_time - start_time

# Measure the time taken to delete 100000 elements from the list
start_time = time.time()
for i in range(100000):
    del lst[i]
end_time = time.time()
list_del_time = end_time - start_time

# Print the dictionary and list delete times
print(f"delete 100000 elements from dictionary: {dict_del_time:.6f} seconds")
print(f"delete 100000 elements from list: {list_del_time:.6f} seconds")
