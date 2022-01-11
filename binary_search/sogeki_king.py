'''
https://atcoder.jp/contests/abc023/tasks/abc023_d
'''

'''
n = int(input())
conditions = [tuple(map(int, input().split())) for _ in range(n)]
'''
n = 6
conditions = [(100, 1), (100, 1), (100, 1), (100, 1), (100, 1), (1, 30)]

def ok(x):
    limit = [(x-h)/s for h, s in conditions]
    limit.sort()
    for i in range(n):
        if limit[i] < i:
            return False
    return True

lo, hi =0, 2e14
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid):
        hi = mid
    else:
        lo = mid + 1

print(int(lo))