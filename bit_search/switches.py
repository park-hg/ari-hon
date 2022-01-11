'''
https://atcoder.jp/contests/abc128/tasks/abc128_c
'''

n, m = 5, 2
switch = [[3, 1, 2, 5], [2, 2, 3]]
p = [1, 0]
'''
n, m = map(int, input().split())
switch = []
for _ in range(m):
    switch.append(list(map(int, input().split())))
p = list(map(int, input().split()))
'''

onoff = [[0] * n for _ in range(m)]


for i in range(m):
    for idx in switch[i][1:]:
        onoff[i][idx-1] = 1

ans = 0
for i in range(1 << n):
    d = True
    for j in range(m):
        c = 0
        for k in range(n):
            if (i >> k) & onoff[j][n-k-1]:
                c += 1
        if c % 2 != p[j]:
            d *= False
    if d:
        ans += 1
print(ans)