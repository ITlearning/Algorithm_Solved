# 안전영역
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y,target):
    for cur in range(4):
        nx = x + dx[cur]
        ny = y + dy[cur]
        if (0 <= nx < N) and (0 <= ny < N) and not dist[nx][ny] and board[nx][ny] > target:
            dist[nx][ny] = True
            dfs(nx,ny,target)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 1
for k in range(max(map(max, board))):
    dist = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > k and not dist[i][j]:
                cnt += 1
                dist[i][j] = True
                dfs(i,j,k)
    ans = max(ans,cnt)
print(ans)