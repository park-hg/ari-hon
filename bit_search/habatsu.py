'''
https://atcoder.jp/contests/abc002/tasks/abc002_4
'''
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    A.append([x-1, y-1])

def check(bit):
    for i in range(N-1):
        for j in range(i+1, N):
            if bit & (1 << i) and bit & (1 << j):
                if [i, j] not in A:
                    return False
    return True

ans = 0
for bit in range(1 << N):
    if check(bit):
        cnt = 0
        num = bit
        while num:
            num &= num-1
            cnt += 1
        ans = max(ans, cnt)

print(ans)