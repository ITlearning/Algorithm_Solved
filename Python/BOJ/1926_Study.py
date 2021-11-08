# 그림
from collections import deque
n,m = map(int,input().split())

board = []
dx = [0,-1,0,1]
dy = [-1,0,1,0]

for i in range(n):
    board.append(list(map(int,input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]
answer_cnt = 0
answer_box = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 or visited[i][j] == True:
            continue
        answer_cnt += 1
        q = deque()
        q.append([i,j])
        cnt = 1
        visited[i][j] = True
        while q:
            x,y = q.popleft()
            for index in range(4):
                nx = x + dx[index]
                ny = y + dy[index]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] == True or board[nx][ny] == 0:
                    continue
                visited[nx][ny] = True
                q.append([nx,ny])
                cnt += 1
        
        answer_box = max(answer_box,cnt)

print(answer_cnt)
print(answer_box)