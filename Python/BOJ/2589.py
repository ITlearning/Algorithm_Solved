# 보물섬
from collections import deque

dx = [0,-1,0,1]
dy = [-1,0,1,0]

n,m = map(int,input().split())
board = []

deque_l = deque()
cnt = 0

# 리스트를 입력 받으면서 L의 좌표 deque_l 에 저장
for i in range(n):
    tmp = list(input())
    board.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == "L":
            deque_l.append([i,j])


def bfs(x,y):
    q = deque()
    q.append([x,y])
    distance = [[-1]*m for _ in range(n)]
    
    distance[x][y] = 0
    result = 0

    while q:
        x,y = q.popleft()
        for cur in range(4):
            nx = x + dx[cur]
            ny = y + dy[cur]
            if 0 <= nx < n and 0 <= ny < m:
                # 탐색하는 위치에 L이 존재하고, 방문하지 않았다면
                if board[nx][ny] == "L" and distance[nx][ny] == -1:
                    # 거리 늘려주고 result에 값 비교해서 답 갱신
                    distance[nx][ny] = distance[x][y] + 1
                    result = max(result, distance[nx][ny])
                    # q 덱에 현재 위치 저장
                    q.append([nx,ny])
    
    return result

# L의 위치를 다 저장시켰던 덱을 돌리면서 while 문 시작
while deque_l:
    x,y = deque_l.popleft()
    # bfs 돌린 값과, 현재 cnt 값 비교해서 갱신
    cnt = max(cnt, bfs(x,y))

# 답 도출
print(cnt)

