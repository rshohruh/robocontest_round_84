from bisect import bisect_left, bisect_right

def lower_bound(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


n, m = map(int, input().split())
a = []
b = []
c = []

for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append((ai, bi))

a.sort()
b.sort()

for i in range(n):
    ai, bi = c[i]
    result = upper_bound(a, bi) - lower_bound(b, ai) - 1
    print(result)