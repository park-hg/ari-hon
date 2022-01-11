'''
https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b
'''
import sys


sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
h = [0]*N
h[0], h[1] = 0, a[0]
for i in range(2, N):
    if a[i-1] > h[i-1]:
        h[i] = a[i-1]
    else:
        h[i] = h[i-1]

def func(bit):
    a_new, height, price = a[:], 0, 0
    for i in range(N):
        if bit & (1 << i):
            if max(height, h[i]) >= a[i]:
                height = max(height, h[i]) + 1
                a_new[i] = height
                price += height - a[i]
            else:
                height = a[i]
    return a_new, price

ans = sys.maxsize
for bit in range(1 << N):
    a_new, price = func(bit)
    cnt, height = 0, 0
    for i in range(N):
        if a_new[i] > height:
            cnt += 1
            height = a_new[i]
    if cnt >= K:
        ans = min(ans, price)

print(ans)