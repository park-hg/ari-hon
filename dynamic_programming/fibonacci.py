n = 3

def brute_force(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return brute_force(n-1) + brute_force(n-2)



from collections import defaultdict

dp2 = defaultdict(int)

def memoization(n):
    if n <= 1:
        return 1
    if dp2[n]:
        return dp2[n]
    dp2[n] = memoization(n-1) + memoization(n-2)
    return dp2[n]

def tabulation(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    dp = [1] * (n + 1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]