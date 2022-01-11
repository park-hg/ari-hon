n = 3
l = [3, 4, 5, 1, 2]

ans = 0
while len(l) > 1:
    l.sort()
    ans += sum(l[:2])
    l = l[2:] + [sum(l[:2])]

print(ans)