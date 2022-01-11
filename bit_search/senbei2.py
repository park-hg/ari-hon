'''
https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e
'''
# different solution

r, c = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(r)]

ans = 0
for i in range(2**r):
    all_count = 0
    for j in range(c):
        count = 0
        for k in range(r):
            count += (plate[k][j] + ((i>>k)&1))%2
        all_count += max(count, r-count)
    ans = max(ans, all_count)

print(ans)