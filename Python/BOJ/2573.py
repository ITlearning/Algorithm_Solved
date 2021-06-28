# 빙산
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,-1,0,1]
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dist = [[False for _ in range(M)] for _ in range(N)]
cnt = 0
new_board = [[0 for _ in range(M)] for _ in range(N)]
def check(i,j):
    x = i
    y = j
    z_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0:
                z_cnt += 1
    return z_cnt

def dfs(x,y):
    dist[x][y] = 1
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 0 or dist[nx][ny] == True:
                continue
            dist[nx][ny] = True
            q.append((nx,ny))


def melt():
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                return False
    return True

box = 0
time = 0
while True:
    q = deque()
    cnt = 0
    for v in range(N):
        for d in range(M):
            if board[v][d] > 0 and dist[v][d] == False:
                cnt += 1
                dfs(v,d)
    box = max(box, cnt)
    if box >= 2:
        break
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                z = check(i,j)
                if board[i][j] - z < 0:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = board[i][j] - z
    board = new_board[:]
    new_board = [[0 for _ in range(M)] for _ in range(N)]
    dist = [[False for _ in range(M)] for _ in range(N)]
    if melt():
        time = 0
        break
    # DFS 시작
    time += 1

print(time)
    
