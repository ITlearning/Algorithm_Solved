import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

M = int(input())
board = list(map(int,input().split()))

N = int(input())
dist = list(map(int, input().split()))


def count_range(a, left, right):
    left = bisect_left(a,right)
    right = bisect_right(a,left)
    return right - left

for i in dist:
    tmp = count_range(board,i,i)
    print(tmp)