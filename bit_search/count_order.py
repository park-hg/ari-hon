'''
https://atcoder.jp/contests/abc150/tasks/abc150_c
'''

n = 8
p = (7, 3, 5, 4, 2, 1, 6, 8)
p = tuple(i-1 for i in p)
q = (3, 8, 2, 5, 4, 6, 7, 1)
q = tuple(i-1 for i in q)

from itertools import permutations
import math

n = int(input())
p = tuple(map(int, input().split()))
p = tuple(i-1 for i in p)
q = tuple(map(int, input().split()))
q = tuple(i-1 for i in q)
permus = list(permutations(range(n)))
for i in range(math.factorial(n)):
    if permus[i] == p:
        a = i
    if permus[i] == q:
        b = i

print(abs(a-b))