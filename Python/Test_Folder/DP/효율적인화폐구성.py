n,m = map(int,input().split())
board = []

for i in range(n):
    board.append(int(input()))


d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(board[i], m+1):
        if d[j-board[i]] != 10001:
            d[j] = min(d[j], d[j-board[i]]+1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])