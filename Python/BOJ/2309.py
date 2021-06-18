# 일곱 난쟁이
import sys
input = sys.stdin.readline
board = []
for _ in range(9):
    board.append(int(input()))
board.sort()
tmp = 0
cursor = 0
one, two = 0,0
for i in range(len(board)):
    for j in range(len(board)):
        tmp = sum(board) - (board[i]+board[j])
        if tmp == 100:
            one = i
            two = j
board.pop(one)
board.pop(two)
for i in range(len(board)):
    print(board[i])