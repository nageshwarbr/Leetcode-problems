def insertionSort(A):
    n = len(A)
    for i in range(1, n ):
        value = A[i]
        hole = i
        while hole > 0 and A[hole - 1] > value:
            A[hole] = A[hole - 1]
            hole = hole - 1
        A[hole] = value
    return A


lst = [2, 5, 3, 1, 7, 4]
print(insertionSort(lst))
