'''
https://atcoder.jp/contests/abc145/tasks/abc145_c
'''

n = 3
position = [[0, 0], [1, 0], [0, 1]]

from itertools import permutations
import math

dis = count = 0
for path in permutations(range(n)):
    for i in range(n-1):
        d = 0
        for j in range(2):
            d += (position[path[i+1]][j] - position[path[i]][j])**2
        dis += math.sqrt(d)
    count += 1

print(dis/count)