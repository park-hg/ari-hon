n = 2
a = [1,5]
b = [2,4]
c = [3,6]

a.sort()
b.sort()
c.sort()

import bisect

ans = 0
for mid in b:
    idx_a = bisect.bisect_left(a, mid)
    idx_c = bisect.bisect_right(c, mid)
    ans += (idx_a) * (n - idx_c)

print(ans)