# 알고스팟
from collections import deque

n,m = map(int, input().split())
board = []

dx = [0,-1,0,1]
dy = [-1,0,1,0]

for _ in range(m):
    tmp = list(input())
    board.append(tmp) 

dist = [[-1 for _ in range(n)] for _ in range(m)]
dist[0][0] = 0

q = deque()

q.append([0,0])

while q:
    x,y = q.popleft()
    for cur in range(4):
        nx = x + dx[cur]
        ny = y + dy[cur]
        if 0 <= nx < m and 0 <= ny < n:
            # 아직 방문하지 않은 리스트라면
            if dist[nx][ny] == -1:
                # 그 위치가 0 숫자라면
                if board[nx][ny] == '0':
                    # 덱의 앞에 위치시켜서 우선순위를 높혀줌
                    q.appendleft([nx,ny])
                    # 그리고 거리 값은 갱신하지 않음 (+1 하지 않는다는 의미)
                    dist[nx][ny] = dist[x][y]
                # 그 위치가 1 숫자라면
                elif board[nx][ny] == '1':
                    # 덱의 뒤에 위치시켜 0보다는 우선순위가 낮게 설정하여 최적의 거리를 탐색
                    q.append([nx,ny])
                    # 이 경우에는 뚫고 지나간 경우니 +1 해줌
                    dist[nx][ny] = dist[x][y] + 1

# 답 도출
print(dist[m-1][n-1])
