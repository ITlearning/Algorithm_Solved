# 사탕 게임
N = int(input())

board = []

for _ in range(N):
    board.append(list(input().rstrip()))

# 체크
def check(col,col_move, row, row_move):
    result = 1

    # row check
    for i in range(col, col_move+1):
        row_tmp = 1
        for j in range(1,N):
            # 체크해서 같으면 카운트
            if board[i][j] == board[i][j-1]:
                row_tmp += 1
            else:
                # 그러다가 하나라도 다른거 나오면 다시 카운트 (같은게 끝났으니)
                row_tmp = 1
            # 그렇게 해서 나온 숫자 계속 업데이트
            result = max(result, row_tmp)
    
    # col check
    for j in range(row, row_move+1):
        col_tmp = 1
        for i in range(1,N):
            # 체크해서 같으면 카운트
            if board[i-1][j] == board[i][j]:
                col_tmp += 1
            else:
                # 그러다가 하나라도 다른거 나오면 다시 카운트 (같은게 끝났으니)
                col_tmp = 1
            # 그렇게 해서 나온 숫자 계속 업데이트
            result = max(result,col_tmp)

    return result

answer = 0

for i in range(N):
    for j in range(N):
        # row 변환
        if j < N-1:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer,check(i,i,j, j+1))
            # 상태 복구
            board[i][j+1], board[i][j] = board[i][j], board[i][j+1]

        # col 변환
        if i < N-1:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer,check(i,i+1,j,j))
            # 상태 복구
            board[i+1][j], board[i][j] = board[i][j], board[i+1][j]

print(answer)
        