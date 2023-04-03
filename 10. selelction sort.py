import sys

A = [64,25,12,22,11]

for i in range(len(A)):
    minValueIndex = i
    for j in range(i+1, len(A)):
        if A[minValueIndex] > A[j]:
            minValueIndex = j
    A[i], A[minValueIndex] = A[minValueIndex], A[i]

print(A)
