n = 5
s = [1, 2, 4, 6, 8]
t = [3, 5, 7, 9, 10]

jobs = []
for i in range(n):
    jobs.append((t[i], s[i]))

jobs.sort()


ans = 1
q = jobs[0][0]
while q < jobs[-1][0]:
    for i in range(n):
        if jobs[i][1] >= q:
            q = jobs[i][0]
            ans += 1
print(ans)

""""""""""""""""""""


ans, q = 0, 0
for i in range(n):
    if q < jobs[i][1]:
        ans += 1
        q = jobs[i][0]
print(ans)