n = 6
r = 10
x = [1, 7, 15, 20, 30, 50]

i = 0
ans = 0
while i < n:
    point = x[i]
    while i < n and x[i] <= point + r:
        i += 1
    mark = x[i - 1]
    while i < n and x[i] <= mark + r:
        i += 1
    ans += 1
    
print(ans)