# 배열 돌리기 1
N,M,R = map(int,input().split())

board = []

for i in range(N):
    board.append(list(map(int,input().split())))

mid = min(N,M) // 2

def rotate(start_row, end_row, start_col, end_col):
    # 각 끝의 숫자 가져오기
    left_top = board[start_col][start_row]
    left_bottom = board[end_col-1][start_row]
    right_top = board[start_col][end_row-1]
    right_bottom = board[end_col-1][end_row-1]
    
    # 돌리기
    # 하
    old_down_num = [left_top]
    for down_index in range(start_col, end_col-1):
        old_down_num.append(board[down_index+1][start_row])
        board[down_index+1][start_row] = old_down_num.pop(0)
    old_down_num.clear()

    # 우
    old_right_num = [left_bottom]
    for right_index in range(start_row, end_row-1):
        old_right_num.append(board[end_col-1][right_index+1])
        board[end_col-1][right_index+1] = old_right_num.pop(0)
    old_right_num.clear()

    # 상
    old_top_num = [right_bottom]
    for top_index in range(end_col-1, start_col, -1):
        old_top_num.append(board[top_index-1][end_row-1])
        board[top_index-1][end_row-1] = old_top_num.pop(0)
    old_top_num.clear()

    # 좌
    old_left_num = [right_top]
    for left_index in range(end_row-1, start_row, -1):
        old_left_num.append(board[start_col][left_index-1])
        board[start_col][left_index-1] = old_left_num.pop(0)
    old_left_num.clear()




for _ in range(R):
    for i in range(mid):
        start_row, end_row = i, M-i
        start_col, end_col = i, N-i
        rotate(start_row, end_row, start_col, end_col)

for bo in board:
    print(*bo)

# Python 3 = 시간 초과
# PyPy 3 = 1416m