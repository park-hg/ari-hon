'''
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
'''
n = 5
a = [1, 5, 7, 10, 21]
q = 4
m = [2, 4, 17, 8]

results = ['No'] * q
def bit_search(target):
    for i in range(2**n):
        ans = 0
        for j in range(n):
            if (i >> j) & 1:
                ans += a[j]
        if target == ans:
            return 'Yes'
    return 'No'

for k in range(q):
    for i in range(2**n):
        ans = 0
        for j in range(n):
            if (i >> j) & 1:
                ans += a[j]
        if m[k] == ans:
            results[k] = 'Yes'

print(results)