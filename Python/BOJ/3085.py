# 사탕 게임
import sys
input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
    text = list(input().rstrip())
    board.append(list(text))

def check(board, s_row, e_row, s_col, e_col):
    n = len(board)
    result = 1
    for i in range(s_row, e_row+1):
        cnt = 1
        for j in range(1, n):
            if board[i][j-1] == board[i][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt

    for i in range(s_col, e_col+1):
        cnt = 1
        for j in range(1,n):
            if board[j-1][i] == board[j][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt

    return result

result = 0
for i in range(n):
    for j in range(n):
        if j < n-1:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            tmp = check(board, i, i,j,j+1)
            if tmp > result:
                result = tmp
            board[i][j+1],board[i][j] = board[i][j], board[i][j+1]

        if i < n-1:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            tmp = check(board,i,i+1, j,j)
            if tmp > result:
                result = tmp
            board[i+1][j], board[i][j] = board[i][j], board[i+1][j]

print(result)

