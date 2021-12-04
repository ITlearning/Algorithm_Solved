# 단지번호붙이기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

board = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]
dist = [[0 for i in range(N)] for i in range(N)]

# 입력값 저장
for i in range(N):
    board.append(list(input().rstrip()))

def bfs(x,y):
    q = deque()
    q.append((x,y))
    m = 1   # 박스의 크기 check
    dist[x][y] = 1  # 방문 여부 갱신
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if board[nx][ny] == '0' or dist[nx][ny] == 1:
                continue
            dist[nx][ny] = 1
            m += 1
            q.append((nx,ny))
    
    return m

cnt = 0  # 전체 횟수
box = [] # 각 박스의 크기 입력 리스트

# 여기서 시작
for i in range(N):
    for j in range(N):
        # 만일 박스(1)이고, 방문하지 않았다면
        if board[i][j] == '1' and dist[i][j] == 0:
            size = bfs(i,j)  # bfs 시작
            cnt += 1
            box.append(size)

print(cnt)
box.sort()
for i in box:
    print(i)
