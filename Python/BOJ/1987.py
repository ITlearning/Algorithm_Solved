# 알파벳
import sys
dx = [0,0,-1,1]
dy = [-1,1,0,0]
input = sys.stdin.readline
# r = 세로, c = 가로
r,c = map(int,input().split())
arr = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(r)]
alpha = [0] * 26
answer = 1
def dfs(x,y, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
        if alpha[arr[nx][ny]] == 1: continue
        alpha[arr[nx][ny]] = 1
        dfs(nx,ny,cnt + 1)
        alpha[arr[nx][ny]] = 0


alpha[arr[0][0]] = 1
dfs(0,0,1)
print(answer)