def mergesort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        print(left, right)
        mergesort(left)
        mergesort(right)
        i = 0
        j = 0
        k = 0
        ans = []
        while i < len(left) and j < len(right):
            print(left, right)
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
                k += 1
            else:
                A[k] = right[j]
                j += 1
                k += 1
        print('***', ans)
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
        


lst = [2, 5, 3, 1, 7, 4]
mergesort(lst)
print(lst)
