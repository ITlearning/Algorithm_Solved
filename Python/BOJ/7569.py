# 토마토
import sys
from collections import deque
input = sys.stdin.readline
# M 상자의 가로 칸 수 , N 상자의 세로 칸 수 , H 쌓아올리는 상자의 수
M,N,H = map(int,input().split())
board = []
dx = [-1,0,1,0,0,0]
dy = [0,-1,0,1,0,0]
dz = [0,0,0,0,-1,1]
for i in range(H):
    tmp = []
    for a in range(N):
        tmp.append(list(map(int,input().split())))
    board.append(tmp)
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                q.append((i,j,k))

while q:
    z,x,y = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= N or ny >= M or nz >= H:
            continue
        if board[nz][nx][ny] == 0:
            board[nz][nx][ny] = board[z][x][y] + 1
            q.append((nz,nx,ny))

t = False
answer = -2
for z in board:
    for x in z:
        for y in x:
            if y == 0:
                t = True
            answer = max(answer, y)

if t:
    print(-1)
else:
    print(answer-1)