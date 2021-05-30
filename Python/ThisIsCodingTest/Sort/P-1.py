# 위에서 아래로

n = int(input())
board = []
for _ in range(n):
    board.append(int(input()))

board.sort(reverse=True)

for i in board:
    print(i, end=' ')