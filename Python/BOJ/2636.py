# 치즈
from collections import deque
dx = [0,-1,0,1]
dy = [-1,0,1,0]
board = []

# n,m 입력받기
n,m = map(int,input().split())

# 보드 입력받기
for i in range(n):
    board.append(list(map(int,input().split())))

cnt = 0 # 지운 횟수
one = 0 # 다 지우기 전 1 개수

while True:
    dist = [[0 for _ in range(m)] for _ in range(n)]
    check = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0,0])
    dist[0][0] = 2
    # 1. BFS 돌면서 바깥쪽 0 체크
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 1 or dist[nx][ny] != 0:
                continue
            dist[nx][ny] = dist[x][y]
            q.append([nx,ny])
    
    t = False
    # 2. 1 개수 카운트
    one_count = 0    
    for b in board:
        for index in b:
            if index == 1:
                one_count += 1

    # 3.BFS 결과를 바탕으로 외부에 노출된 치즈 제거 
    for i in range(n):
        for j in range(m):

            # 외부 공기가 아닌 0은 건너뛰기
            if dist[i][j] != 2:
                continue
            # 상
            if i-1 >= 0:
                if board[i-1][j] == 1 and check[i-1][j] == 0:
                    check[i-1][j] = 1
                    board[i-1][j] = 0
                    t = True
            # 하
            if i+1 < n:
                if board[i+1][j] == 1 and check[i+1][j] == 0:
                    check[i+1][j] = 1
                    board[i+1][j] = 0
                    t = True
            # 좌
            if j-1 >= 0:
                if board[i][j-1] == 1 and check[i][j-1] == 0:
                    check[i][j-1] = 1
                    board[i][j-1] = 0
                    t = True
            # 우
            if j+1 < m:
                if board[i][j+1] == 1 and check[i][j+1] == 0:
                    check[i][j+1] = 1
                    board[i][j+1] = 0
                    t = True
    
    # one_count 가 0 이라는 소리는 더이상 1이 없다라는 소리
    # 4. 따라서 0이 되기전까지는 1의 개수를 전역 변수 one에 넣어주기
    if one_count != 0:
        one = one_count

    # 5
    # 돌아서 바꾼게 있으면 True
    # 돌아서 바꾼게 없으면 False
    if t:
        cnt += 1
    else:
        break                 

print(cnt)
print(one)