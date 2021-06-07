from collections import deque

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]


def solution(n, computers):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 0:
                dist[i][j] = 0

    q = []
    q = deque(q)
    cnt = 0            
    for a in range(n):
        for b in range(n):
            if computers[a][b] == 0 or dist[a][b] != -1: continue
            cnt += 1
            q.append([a,b])
            dist[a][b] = 1
            while q:
                x,y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                    if computers[nx][ny] == 0 or dist[nx][ny] != -1: continue
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
    

    
    return cnt

print(solution(n, computers))