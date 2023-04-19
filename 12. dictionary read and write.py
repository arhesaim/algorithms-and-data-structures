import time

# Initialize an empty dictionary
d = {}

# Measure the time taken to write 1000000 elements to the dictionary
start_time = time.time()
for i in range(1000000):
    d[i] = i
end_time = time.time()
write_time = end_time - start_time

# Measure the time taken to get 1000000 elements from the dictionary
start_time = time.time()
for i in range(1000000):
    x = d[i]
end_time = time.time()
read_time = end_time - start_time

# Print the write and read times
print(f"Write: {write_time:.3f} seconds")
print(f"Read: {read_time:.3f} seconds")