# 이차원 배열과 연산
import copy
from collections import Counter
r,c,k = map(int,input().split())

board = []
for i in range(3):
    tmp = list(map(int,input().split()))
    board.append(tmp)

cnt = 1

def rebuild(board, command):
    if command == "C":
        board = list(map(list, zip(*board)))
    
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
        
    # 크기 다른거 0 채우기
    for rebuild in range(len(board)):
        if len(board[rebuild]) < max_len:
            board[rebuild] += [0] * (max_len - len(board[rebuild]))
    if command == "C":
        board = list(map(list, zip(*board)))
    return board


for i in range(101):
    if r-1 < len(board) and c-1 < len(board[0]) and board[r-1][c-1] == k:
        print(i)
        exit(0)

    if len(board) >= len(board[0]):
        board = rebuild(board,"R")
    else:
        board = rebuild(board,"C")

print(-1)
