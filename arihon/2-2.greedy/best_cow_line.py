s = 'acdbcb'
n = 6

t = ''
while s:
    # if s[0] < s[-1]:
    if s < s[::-1]:
        t += s[0]
        s = s[1:]
    else:
        t += s[-1]
        s = s[:-1]
print(t)