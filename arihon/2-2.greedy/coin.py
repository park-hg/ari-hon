c = [3, 2, 1, 3, 0, 2]
v = [1, 5, 10, 50, 100, 500]
a = 620

ans = 0
for i in range(len(c)-1,-1,-1):
    t = min(a // v[i], c[i])
    a -= t * v[i]
    ans += t

print(ans)