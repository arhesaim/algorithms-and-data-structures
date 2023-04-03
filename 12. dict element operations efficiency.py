import timeit

dictionary = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f"}

def dictAddFirst(dictionary):
    dictionary[1] = "A"

def dictAddLast(dictionary):
    dictionary[7] = "g"

def dictGetFirst(dictionary):
    dictionary[1]

def dictGetLast(dictionary):
    dictionary[7]


def dictAddFirstTime():
    mySetup = '''
from __main__ import dictAddFirst
from __main__ import dictionary'''
    testCode = '''dictAddFirst(dictionary)'''
    print(timeit.timeit(setup= mySetup, stmt= testCode, number= 1))

def dictAddLastTime():
    mySetup = '''
from __main__ import dictAddLast
from __main__ import dictionary'''
    testCode = '''dictAddLast(dictionary)'''
    print(timeit.timeit(setup= mySetup, stmt= testCode, number= 1))

def dictGetFirstTime():
    mySetup = '''
from __main__ import dictGetFirst
from __main__ import dictionary'''
    testCode = '''dictGetFirst(dictionary)'''
    print(timeit.timeit(setup= mySetup, stmt= testCode, number= 1))

def dictGetLastTime():
    mySetup = '''
from __main__ import dictGetLast
from __main__ import dictionary'''
    testCode = '''dictGetLast(dictionary)'''
    print(timeit.timeit(setup= mySetup, stmt= testCode, number= 1))

if __name__ == "__main__":
    dictAddFirstTime()
    dictAddLastTime()
    dictGetFirstTime()
    dictGetLastTime()