# 단지번호 붙이기
import sys
input = sys.stdin.readline
N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
number = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]
cnt = 0

def dfs(x,y):
    global cnt
    board[x][y] = '0'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[nx][ny] == '1':
            dfs(nx,ny)


for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            cnt = 0
            dfs(i,j)
            number.append(cnt)

print(len(number))
number.sort()
for i in number:
    print(i)