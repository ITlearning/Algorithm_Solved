from collections import deque
N,M = map(int,input().split())

board = []
dist = [[0]*(M) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for i in range(N):
    board.append(list(input().rstrip()))

dist[0][0] = 1
q = deque()
q.append((0,0))
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == '0' or dist[nx][ny] > 1:
            continue
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))

print(dist[N-1][M-1])