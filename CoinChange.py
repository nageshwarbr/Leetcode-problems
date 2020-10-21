def count(S, m, n):
    table = [0] * (n + 1)

    minimum = 100000
    table[0] = 1
    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]

    return table[n]


arr = [1, 3, 2]
m = len(arr)
n = 4
x = count(arr, m, n)
print(x)
