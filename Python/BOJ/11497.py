# 통나무 건너뛰기
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    board = [int(x) for x in input().split()]
    board.sort()

    max_level = 0
    for i in range(2,n):
        max_level = max(max_level, abs(board[i] - board[i-2]))
        print(max_level)

    #print(max_level)
