'''
https://atcoder.jp/contests/abc147/tasks/abc147_c
'''

import sys
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
A = [[] for _ in range(n)]
for i in range(n):
    m = int(sys.stdin.readline())
    for _ in range(m):
        x, y = list(map(int, sys.stdin.readline().split()))
        A[i].append([x-1, y])


def check(bit):
    for i in range(n):
        if (bit & (1 << i)):
            for x, y in A[i]:
                if y == 1 and not(bit & (1 << x)):
                    return False
                if y == 0 and (bit & (1 << x)):
                    return False
    return True

ans = 0
for bit in range(1 << n):
    if check(bit):
        cnt = 0
        for i in range(n):
            if bit & (1 << i):
                cnt += 1
        ans = max(ans, cnt)
print(ans)