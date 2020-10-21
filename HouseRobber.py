def house_robber(list1):
    n = len(list1)
    if n == 0:
        return 0

    dp = [0] * n
    dp[0] = list1[0]
    for i in range(1, n):
        if i == 1:
            dp[i] = max(list1[0], list1[1])
        else:
            dp[i] = max(dp[i - 1], list1[i] + dp[i - 2])

    return dp[-1]


l = [1, 2, 3, 1]
print(house_robber(l))
