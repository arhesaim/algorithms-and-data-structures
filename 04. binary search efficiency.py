import timeit
#import matplotlib.pyplot as plt
import random as rd

k = 1

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    k += 1

    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# def plot_time(list, time):
#     plt.plot(range(0, len(list), 1), range(0, time, 1))

random_list = []

for i in range(0, 5000):
    value = rd.randint(1, 5000)
    random_list.append(value)


def binary_time():
    mysetup = '''
from __main__ import binary_search
from __main__ import random_list'''
    TEST_CODE = '''binary_search(random_list, 3)'''
    print(timeit.timeit(setup=mysetup, stmt=TEST_CODE, number= 1000000))

list_forGraph = len(random_list)/k
time_forGraph = binary_time()/k


if __name__ == "__main__":
    binary_time()