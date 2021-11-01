# 사탕 게임
N = int(input())

board = []

for _ in range(N):
    board.append(list(input().rstrip()))

def check(col,col_move, row, row_move):
    result = 1
    # row check
    for i in range(col, col_move+1):
        row_tmp = 1
        for j in range(1,N):
            if board[i][j] == board[i][j-1]:
                row_tmp += 1
            else:
                row_tmp = 1
            result = max(result, row_tmp)
    
    # col check
    for j in range(row, row_move+1):
        col_tmp = 1
        for i in range(1,N):
            if board[i-1][j] == board[i][j]:
                col_tmp += 1
            else:
                col_tmp = 1
            result = max(result,col_tmp)

    return result

answer = 0

for i in range(N):
    for j in range(N):
        # row 변환
        if j < N-1:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer,check(i,i,j, j+1))
            board[i][j+1], board[i][j] = board[i][j], board[i][j+1]

        # col 변환
        if i < N-1:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer,check(i,i+1,j,j))
            board[i+1][j], board[i][j] = board[i][j], board[i+1][j]

print(answer)
        