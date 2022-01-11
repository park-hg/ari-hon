'''
d = 20
n = 4
m = 4
store = [12, 8, 16]
deliver = [7, 7, 11, 8]
'''
d = int(input())
n = int(input())
m = int(input())
store = list(int(input()) for _ in range(n-1))
store.extend([0, d])
deliver = list(int(input()) for _ in range(m))

import bisect

store.sort()

ans = 0
for point in deliver:
    idx = bisect.bisect_left(store, point)
    ans += min(abs(store[idx]-point), abs(point-store[idx-1]))
print(ans)


    
def bisearch(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid+1
        elif a[mid] > x:
            high = mid-1
        else:
            return mid
    return low
 
output = 0
for target in deliver:
    idx = bisearch(store, target)
    output += min(abs(store[idx]-target), abs(target-store[idx-1]))
print(output)