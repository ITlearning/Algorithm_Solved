# 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
board = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(n):
    board.append(list(map(int,input().rstrip())))

# 3차원 안에 카운트, 벽을 부순 여부 확인 하는 용도의 2가지 리스트 만들어주기
dist = [[[0] * 2 for i in range(m)]for i in range(n)]

q = deque()
q.append([0,0,1])

dist[0][0][1] = 1
answer = -2

while q:
    x,y,w = q.popleft()

    if x == n-1 and y == m-1:
        answer = dist[x][y][w]
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 벽이 있고, 아직 벽을 뚫고 나가지는 않은 상태
        if board[nx][ny] == 1 and w == 1:
            # 1을 뚫고 들어왔으니까 이제 약간 T,F 역할을 해주는 w를 0으로 만들어주고
            q.append([nx,ny,0])
            # 뚫기전까지 카운트 했던 크기를 0배열에 넣어주는 작업
            dist[nx][ny][0] = dist[x][y][1] + 1
        elif board[nx][ny] == 0 and dist[nx][ny][w] == 0:
            # 그다음부터는 이 코드가 계속 실행
            q.append([nx,ny,w])
            dist[nx][ny][w] = dist[x][y][w] + 1
    
if answer == -2:
    print(-1)
else:
    print(answer)