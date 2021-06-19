# 빗물
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
oneT = False
twoT = False
result = 0
cnt = 0
box_range = list(map(int,input().split()))
board = [[0]*(m) for _ in range(n)]
for a in range(m):
    for i in range(box_range[a]-1, -1,-1):
        board[i][a] = 1

for i in range(n-1,-1,-1):
    oneT = False
    cnt = 0
    for j in range(m):
        if not oneT and board[i][j] == 1:
            oneT = True
            continue

        if oneT and board[i][j] == 0:
            cnt += 1
            continue

        if oneT and board[i][j] == 1:
            result += cnt
            cnt = 0
print(result)