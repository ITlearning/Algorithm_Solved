# 봄버맨
from collections import deque
from copy import deepcopy
R,C,N = map(int,input().split())
q = deque()
board = []

dx = [0,-1,0,1]
dy = [-1,0,1,0]

# 입력받는것과 동시에 O 위치 덱에 저장
for i in range(R):
    tmp = list(input().rstrip())
    board.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == "O":
            q.append([i,j])

# 전체가 다 O로 되어있는 리스트
all_circle = [["O" for _ in range(C)] for _ in range(R)]
cnt = 0

# cnt가 N이 될때까지 돌리기
while cnt < N:
    # 제일 처음 카운트가 시작했으면
    if cnt == 0:
        # 그냥 카운트 + 1 해주고 continue
        cnt += 1
        continue
    
    # 지금 초 가 홀수면
    if cnt % 2 == 1:
        # 모든 위치 O로 변환해주고 카운트 + 1
        board = deepcopy(all_circle)
        cnt += 1
        continue

    # O 위치 저장했던 덱 가져와서 O위치랑 상하좌우 .으로 바꾸기
    while q:
        x,y = q.popleft()
        board[x][y] = "."
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == 'O':
                    board[nx][ny] = '.'
    
    # 그리고 다시 O 위치 체크
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                q.append([i,j])

    # 카운트 + 1
    cnt += 1
    
# 답 출력
for bo in board:
    print("".join(bo))
    


        
      