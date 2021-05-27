# 문제 - 음료수 얼려 먹기

# BFS로 문제 풀기
'''
from collections import deque
n,m = map(int, input().split())
board = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(n) :
    board.append(list(map(int, input())))
cnt = 0
queue = deque()
for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1 : continue
        cnt += 1
        board[i][j] = 1
        queue.append((i,j))
        while queue :
            x,y = queue.popleft()
            for cur in range(4):
                nx = x + dx[cur]
                ny = y + dy[cur]
                if nx < 0 or nx >= n or ny < 0 or ny >= m : 
                    continue
                if board[nx][ny] == 1:
                    continue
                queue.append((nx,ny))
                board[nx][ny] = 1
print(cnt)
'''

# DFS로 문제 풀기
n,m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) :
            result += 1

print(result)