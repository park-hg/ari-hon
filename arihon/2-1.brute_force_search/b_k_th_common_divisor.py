'''
https://atcoder.jp/contests/abc120/tasks/abc120_b
'''

a, b, k = map(int, input().split())

def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        r = a % b
        a, b = b, r
    return a

g = gcd(a, b)

c = 0
for i in range(g, 0, -1):
    if g % i == 0:
        c += 1
    if c == k:
        print(i)
        break