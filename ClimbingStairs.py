import functools
import math


def climb(n):
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(climb(4))

# Trial
# art = [1, 2, 3, 4, 5, 6, 7, 8, 9]
art = [80, -50, 90, 100]


# def maxSum(k, l1):
#     currentMax = -math.inf
#     n = len(l1)
#     for i in range(0, n - k + 1):
#         currentMax = max(functools.reduce(lambda a, b: a + b, l1[i:i+k]), currentMax)
#         print(currentMax, i)
#     print(currentMax, i)
#
#
# maxSum(2, art)

# print(functools.reduce(lambda a, b: a + b, art[1:4]))
