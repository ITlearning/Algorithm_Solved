from collections import deque

def dfs(q,n,m,dx,dy,dist,maps):
    q.append((0,0))
    dist[0][0] = 1
    while q:
        x,y = q.popleft()
        if x == n-1 and y == m-1:
            return dist[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0 or dist[nx][ny] >= 1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))
    return -1

def solution(maps):
    answer = 0
    q = deque()
    n = len(maps)
    m = len(maps[0])
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    dist = [[0 for _ in range(m)] for _ in range(n)]
    
    answer = dfs(q,n,m,dx,dy,dist,maps)
    return answer

# 전역변수 어캐쓰냐;;