# 추월
n = int(input())
board = {}
for i in range(1,n+1):
    board[input()] = i

answer = []

min_num = min(board.values())
cnt = 0
for _ in range(n):
    tmp = input()
    if min_num != board[tmp]:
        cnt += 1
        del board[tmp]
    else:
        del board[tmp]
        if board:
            min_num = min(board.values())

print(cnt)