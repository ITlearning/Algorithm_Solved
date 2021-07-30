# 저울
import sys
input = sys.stdin.readline

N = int(input())

board = list(map(int,input().split()))
board.sort()
total = []
for i in range(0,N-1):
    if board[i] not in total:
        total.append(board[i])
    for j in range()