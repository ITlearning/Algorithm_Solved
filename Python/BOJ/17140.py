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
    # C연산으로 들어왔으면 board를 전체 뒤집어줌
    if command == "C":
        board = list(map(list, zip(*board)))
    max_len = 0
    for row_line in range(len(board)):
        new_board = []
        for j in range(len(board[row_line])):
            # 0 이면 안 세도 되니까 넘어감
            if board[row_line][j] == 0:
                continue
            # 0 아니면 일단 추가
            new_board.append(board[row_line][j])
        # Counter로 현재 입력된 것들의 개수 세기
        line = Counter(new_board)
        # 등장횟수가 커지는 순, 그게 아니면 수가 커지는 순으로 정렬한다.
        sort = sorted(line.items(), key=lambda x: (x[1], x[0]))
        tmp = list(sort)
        rebase = []
        # 그리고 정렬된 값 더해주기
        for new in tmp:
            rebase += new
        # 길이가 100 넘어가면 그냥 100으로 길이 지정해주고 끊어줌
        if len(rebase) > 100:
            max_len = 100
        else: max_len = max(max_len, len(rebase)) # 그게 아니면 길이 긴 걸로 업데이트
        board[row_line] = copy.deepcopy(rebase[:100]) # 100 번째까지 복사해서 업데이트

    # 크기 다른거 0 채우기
    for rebuild in range(len(board)):
        if len(board[rebuild]) < max_len:
            board[rebuild] += [0] * (max_len - len(board[rebuild]))
    # 아까 C로 들어왔으면 원상태로 뒤집어주기
    if command == "C":
        board = list(map(list, zip(*board)))
    return board

# 101번 까지 계산해본다.
for i in range(101):
    if r-1 < len(board) and c-1 < len(board[0]) and board[r-1][c-1] == k:
        print(i)
        exit(0)

    if len(board) >= len(board[0]):
        board = rebuild(board,"R")
    else:
        board = rebuild(board,"C")

# 101 번 계산을 해도 안나오면 -1 출력
print(-1)
