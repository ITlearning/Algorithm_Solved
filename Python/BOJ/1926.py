# 그림
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
board = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 입력받기
for i in range(n):
    board.append(list(map(int,input().split())))
dist = [[0]*(m) for _ in range(n)]

cnt = 0 # 그림 개수
big = 0 # 그림 중 가장 큰 수

# bfs 구현 함수
def bfs(x,y):
    cnt = 0
    q = deque()
    q.append((x,y))
    dist[x][y] = 1
    while q:
        cnt += 1
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0 or dist[nx][ny] == 1:
                continue
            dist[nx][ny] = 1
            q.append((nx,ny))
            
    return cnt


t = 0


for i in range(n):
    for j in range(m):
        # 전체 인덱스를 돌면서 1이고 방문하지 않았다면 탐색 시작
        if board[i][j] == 1 and dist[i][j] == 0:
            t += 1
            c = bfs(i,j)
            big = max(big, c)

print(t)
print(big)