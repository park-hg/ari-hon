'''
https://atcoder.jp/contests/abc057/tasks/abc057_c
'''

n = int(input())

ans = float('inf')
root_n = int(math.sqrt(n))
i = 1
while i * i <= n:
    if n % i == 0:
        f = max(len(str(n // i)), len(str(i)))
        ans = min(ans, f)
    i += 1
print(ans)