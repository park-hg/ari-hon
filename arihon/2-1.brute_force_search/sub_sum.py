a = [1,2,4,7]
k = 13

def dynamic(a, k):
    m = sum(a)
    dp = [False] * (m+1)
    dp[a[0]] = True
    for i in range(m+1):
        for j in range(len(a)):
            if dp[i] and i+a[j] <= m:
                dp[i+a[j]] = True

def dfs(i, summation):
    if i == len(a):
        return summation == k
    if dfs(i+1, summation):
        return True
    if dfs(i+1, summation+a[i]):
        return True
    return False
print(dfs(0,0))