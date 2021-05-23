# 이진 탐색하기
# 모듈 안쓰고 구현
mylist = [1,2,3,7,9,11,33]
'''
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

print(bisect(mylist, 3))
'''

# 모듈 쓰고 구현

import bisect
print(bisect.bisect(mylist,3))
