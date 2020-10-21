def bubbleSort(A):
    n = len(A)
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(0, n - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                isSorted = False
        n = n - 1
    return A


lst = [2, 5, 3, 1, 7, 4]
print(bubbleSort(lst))
