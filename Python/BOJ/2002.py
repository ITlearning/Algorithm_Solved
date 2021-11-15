# 추월

n = int(input())
board = {}
pick = []
for i in range(n):
    board[input()] = i+1

for _ in range(n):
    tmp = input()
    pick.append(board[tmp])
    del board[tmp]
    print(board)

print(pick)