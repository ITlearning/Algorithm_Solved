# 뱀
import sys
from collections import deque
input = sys.stdin.readline
    # 우 상 좌 하
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 보드의 크기
n = int(input())
board = [[0 for _ in range(n)]for _ in range(n)]
# 사과의 개수
k = int(input())
for i in range(k):
    x,y = map(int,input().split())
    board[x-1][y-1] = 9

# 뱀의 방향 전환 횟수
l = int(input())
route = deque()
for i in range(l):
    index, turn = input().split()
    route.append([int(index), turn])
# 움직이는 인덱스
x = 0
y = 0
cnt = 0 # 움직인 횟수
cur = 0 # 방향
body = deque() # 몸통 인덱스
# 몸통 덱을 따로 파서, 이동한 위치에 사과가 없으면 꼬리 위치를 0으로 바꿔야 하니
# 위치를 저장시켰다.
board[0][0] = 1
body.append([0,0])

while True:
    # 1. 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
    x += dx[cur]
    y += dy[cur]

    # 벽이나 몸에 머리가 위치했을경우에 지금 횟수에 +1 을 해주고 종료
    if x < 0 or y < 0 or x >= n or y >= n or board[x][y] == 1:
        print(cnt+1)
        break
    
    # 2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고
    # 꼬리는 움직이지 않는다.
    # 3. 사과가 없으면 몸길이를 줄여 꼬리가 위치한 곳의 칸을 비워준다. (몸 길이 불변)
    if board[x][y] == 9: # 사과 있을 때
        board[x][y] = 1
        body.append([x,y])
    elif board[x][y] == 0 : # 없을 때
        if len(body) != 0:
            board[x][y] = 1
            body.append([x,y])
            ix, iy = body.popleft()
            board[ix][iy] = 0
    
    # 카운트 올리기
    cnt += 1

    # 방향 전환
    if len(route) != 0:
        if route[0][0] == cnt:
            time,turn = route.popleft()
            # 오른쪽 이동 시
            if turn == 'D':
                if cur == 0:
                    cur = 3
                else:
                    cur -= 1
            # 왼쪽 이동 시
            if turn == 'L':
                if cur == 3:
                    cur = 0
                else:
                    cur += 1
