# 패션왕 신혜빈
T = int(input())
while T > 0:
    board = {}
    N = int(input())
    total = N
    for i in range(N):
        stuff, category = input().split()
        if category not in board:
            board[category] = 0
        board[category] += 1
    if len(board) > 1:
        tmp = 1
        for i in board.values():
            tmp *= i
        total += tmp
    print(board)
    print(total)
    T -= 1