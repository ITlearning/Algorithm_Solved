# 적록색약
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
board = []
dist = [[0 for i in range(N)] for i in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
q = deque()

# 입력받기
for i in range(N):
    board.append(list(input().rstrip()))

# bfs돌리기
def bfs(x,y):
    q.append((x,y))
    dist[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if board[nx][ny] != board[x][y] or dist[nx][ny] == 1:
                continue
            dist[nx][ny] = 1
            q.append((nx,ny))

# 여기서 시작
cnt = 0
for i in range(N):
    for j in range(N):
        if dist[i][j] == 0:
            bfs(i,j)
            cnt += 1
# 먼저 적록색약이 아닌 사람의 개수
print(cnt,end=' ')

dist = [[0 for i in range(N)] for i in range(N)]

# G를 R로 바꾸어 적록색약 일때의 경우를 체크
for i in range(N):
    for j in range(N):
        if board[i][j] == 'G':
            board[i][j] = 'R'

cnt = 0
for i in range(N):
    for j in range(N):
        if dist[i][j] == 0 :
            bfs(i,j)
            cnt += 1
# 적록색약일 경우의 개수 체크
print(cnt)