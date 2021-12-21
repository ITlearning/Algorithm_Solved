# 현수막
from collections import deque

m,n = map(int,input().split())
board = []

# 상하좌우 + 대각선
dx = [0,-1,0,1,-1,-1,1,1]
dy = [-1,0,1,0,-1,1,-1,1]

# 입력 받기
for _ in range(m):
    board.append(list(map(int,input().split())))

cnt = 0

# 2차원 리스트 하나씩 돌면서
for i in range(m):
    for j in range(n):
        # 현수막이면
        if board[i][j] == 1:
            cnt += 1
            q = deque()
            q.append([i,j])

            # 방문했다라는 표시로 2로 변경
            board[i][j] = 2
            
            # bfs 시작
            while q:
                x,y = q.popleft()
                # 상하좌우 + 대각선 돌면서 
                for direction in range(8):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    if 0 <= nx < m and 0 <= ny < n:
                        # 현수막이면
                        if board[nx][ny] == 1:
                            # 덱에 넣고 
                            q.append([nx,ny])
                            # 방문표시
                            board[nx][ny] = 2

print(cnt)
            