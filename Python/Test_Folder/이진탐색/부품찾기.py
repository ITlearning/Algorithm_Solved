import sys
input = sys.stdin.readline

N = int(input())
board = list(map(int,input().split()))

M = int(input())
check = list(map(int,input().split()))

board.sort()


def binary_search(start, end, target):
    while start <= end:
        mid = (start+end) // 2
        if board[mid] == target:
            return mid
        elif board[mid] > target:
            end = mid - 1
        elif board[mid] < target:
            start = mid + 1
    return -1


for i in check:
    result = binary_search(0, N-1, i)
    if result == -1:
        print("no", end=' ')
    else:
        print("yes", end=' ')