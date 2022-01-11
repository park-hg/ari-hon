a = [-1,0,3,5,9,12]
x = 13

def binary_search(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid
        else:
            return mid
    return -1


b = [1, 1, 2, 2, 2, 3, 4]
y = 2

def bisect_left(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def bisect_right(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo

print(binary_search(a, x))
print(bisect_left(a, x))
print(bisect_right(a, x))

print(binary_search(b, y))
print(bisect_left(b, y))
print(bisect_right(b, y))