'''
https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e
'''
from copy import deepcopy

ans = 0
r, c = map(int, input().split())
plate = []
for _ in range(r):
    plate.append(list(map(int, input().split())))

for i in range(2**r):
    tmp = deepcopy(plate)
    all_count = 0
    for j in range(r):
        if (i>>j)&1:
            tmp[j] = [1-i for i in tmp[j]]
    for k in range(c):
        count = 0
        for l in range(r):
            count += tmp[l][k]
        count = max(count, r-count)
        all_count += count
    ans = max(ans, all_count)

print(ans)