'''
https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
'''

n, m = map(int, input().split())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

sums = 0
for i in range(m):
    for j in range(i + 1, m):
        points = 0
        for k in range(n):
            points += max(a[k][i], a[k][j])
        sums = max(sums, points)

print(sums)