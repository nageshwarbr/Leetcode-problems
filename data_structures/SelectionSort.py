def selectionSort(l1):
    n = len(l1)
    for i in range(0, n - 1):
        minimum = i
        for j in range(i + 1, n):
            if l1[j] < l1[minimum]:
                minimum = j
        l1[i], l1[minimum] = l1[minimum], l1[i]
    return l1


lst = [2, 5, 3, 1, 7, 4]
print(selectionSort(lst))
