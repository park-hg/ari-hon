p = [(2, 3), (1, 2), (3, 4), (2, 2)]
capacity = 5

#############
# brute force
#############

def rec(i, j):
    if i == len(p):
        return 0

    w, v = p[i]
    if j < w:
        return rec(i + 1, j)
    else:
        return max(rec(i + 1, j), rec(i + 1, j - w) + v)

#############
# memoization
#############

# backward
dp = [[0] * (capacity + 1) for _ in range(len(p) + 1)]

for i in range(len(p) - 1, -1, -1):
    for j in range(capacity + 1):
        w, v = p[i]
        if w > j:
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w] + v)


# forward
dp2 = [[0] * (capacity + 1) for _ in range(len(p) + 1)]

for i in range(len(p)):
    #for j in range(capacity, -1, -1): same result
    for j in range(capacity + 1):
        w, v = p[i]
        if w > j:
            dp2[i + 1][j] = dp2[i][j]
        else:
            dp2[i + 1][j] = max(dp2[i][j], dp2[i][j - w] + v)


# reuse matrix
dp3 = [0] * (capacity + 1)

for i in range(len(p)):
    w, v = p[i]
    for j in range(capacity, w - 1, -1):
        dp3[j] = max(dp3[j], dp3[j - w] + v)
print(dp3)