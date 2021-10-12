# 이차원 배열과 연산
import copy
from collections import Counter
r,c,k = map(int,input().split())

board = []
for i in range(3):
    tmp = list(map(int,input().split()))
    board.append(tmp)
cnt = 1
while True:

    row = len(board)
    col = len(board[0])
    if row >= col:
        max_len = 0
        for row_line in range(len(board)):
            new_board = []
            for j in range(len(board[row_line])):
                if board[row_line][j] == 0:
                    continue
                new_board.append(board[row_line][j])
            line = Counter(new_board)
            sort = sorted(line.items(), key=lambda x: (x[1], x[0]))
            tmp = list(sort)
            rebase = []

            for new in tmp:
                rebase += new
            if len(rebase) > 100:
                max_len = 100
            else: max_len = max(max_len, len(rebase))
            board[row_line] = copy.deepcopy(rebase[:100]) 
            #print(tmp)
        # 크기 다른거 0 채우기
        for rebuild in range(len(board)):
            if len(board[rebuild]) < max_len:
                board[rebuild] += [0] * (max_len - len(board[rebuild]))
    elif row < col:
        max_len = 0
        rebuild_col_board = []
        for i in range(len(board[0])):
            tmp = []
            for j in range(len(board)):
                if board[j][i] == 0:
                    continue
                tmp.append(board[j][i])
            col_counter = Counter(tmp)
            sort_counter = sorted(col_counter.items(), key=lambda x: (x[1], x[0]))
            #print(sort_counter)

            list_sort = list(sort_counter)
            rebase = []
            for new in list_sort:
                rebase += new
            if len(rebase) > 100:
                max_len = 100
            else: max_len = max(max_len, len(rebase))

            if len(rebase) < max_len:
                rebase += [0] * (max_len - len(rebase))
            rebuild_col_board.append(rebase)
        total = [[0 for _ in range(len(rebuild_col_board))] for _ in range(len(rebuild_col_board[0]))]

        for i in range(len(rebuild_col_board)):
            for j in range(len(rebuild_col_board[0])):
                total[j][i] = rebuild_col_board[i][j]
        #print(total)
        board = copy.deepcopy(total)
    for i in board:
        print(i)
    print()
    if r-1 < len(board) and c-1 < len(board[0]) and board[r-1][c-1] == k:
        print(cnt)
        break
    cnt += 1
    if cnt > 100:
        print(-1)
        break

