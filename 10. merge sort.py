import random

def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        L = arr[:middle]
        R = arr[middle:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1
        
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = []
    for i in range(500):
        arr.append(random.randint(0,1000))

    printList(arr)
    mergeSort(arr)
    print("//////////////////////////////")
    printList(arr)