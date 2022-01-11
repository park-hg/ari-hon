'''
https://leetcode.com/problems/binary-search/submissions/
'''
nums = [-1,0,3,5,9,12]
target = 9

def recursive(a, x, low, high):
    if low < high:
        mid = (low + high) // 2
        if a[mid] < x:
            return recursive(a, x, mid + 1, high)
        elif a[mid] > x:
            return recursive(a, x, low, mid)
        else:
            return mid
    else:
        return -1

print(recursive(nums, target, 0, len(nums)))

def iterative(a, x):
    low = 0
    high = len(a)
    while low <= high:
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid
        else:
            return mid
    return -1

print(iterative(nums, target))