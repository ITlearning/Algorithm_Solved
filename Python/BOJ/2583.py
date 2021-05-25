m,n,k = map(int,input().split())
board = [[0] * n for _ in range(m)]
dist = [[False] * n for _ in range(m)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
v = []
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1, x2) :
        for j in range(y1,y2):
            board[j][i] = 1

cnt = 0
for i in range(m):
    for j in range(n):
        if board[i][j] or dist[i][j] : continue
        cnt += 1
        box = 0
        queue = [[i,j]]
        dist[i][j] = 1
        while queue:
            x,y = queue[0][0],queue[0][1]
            del queue[0]
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= m or ny < 0 or ny >= n : continue
                if dist[nx][ny] or board[nx][ny] : continue
                dist[nx][ny] = True
                queue.append([nx,ny])
                box += 1
        v.append(box+1)

v = sorted(v)

print(cnt)
for i in v:
    print(i, end=' ')