# Puyo Puyo
from collections import deque
board = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(12):
    tmp = input().rstrip()
    board.append(list(tmp))
total = 0

# 알파벳으로 되어있는 위치 파악
def collection_alphabet():
    global alphabet, board
    for i in range(12):
        for j in range(6):
            if board[i][j] != ".":
                alphabet.append([i,j])

# 각 알파벳들이 이어진 개수 확인
def bfs(i,j):
    global board
    q = deque()
    q.append([i, j])
    change_box.append([i, j])

    while q:
        x, y = q.popleft()
        for cur in range(4):
            nx = x + dx[cur]
            ny = y + dy[cur]
            #print(nx,ny)
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if dist[nx][ny] == True or board[nx][ny] != board[x][y] or board[nx][ny] == ".":
                continue
            dist[nx][ny] = True
            q.append([nx, ny])
            change_box.append([nx, ny])

# 지워진 알파벳 위치에 위에 있는 알파벳들 옮기는 작업
# 이 로직을 이렇게 구현하는지 몰라서 다와서 헤멨음
def move():
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11,j,-1):
                if board[j][i] != "." and board[k][i] == ".":
                    board[k][i] = board[j][i]
                    board[j][i] = "."

# 여기서 while문 시작
while True:
    alphabet = []
    t = False
    # 알파벳 위치 끌어다 모으기
    collection_alphabet()
    
    # 가져온 알파벳들로 하나하나 확인하기
    for i,j in alphabet:
        dist = [[False for _ in range(6)] for _ in range(12)]
        dist[i][j] = True
        change_box = []
        bfs(i,j)
        # 만일 이어진 수가 3개 이상일 경우
        if len(change_box) >= 4:
            t = True
            # 일단 .으로 다 바꿔주고
            while change_box:
                x, y = change_box.pop()
                board[x][y] = "."
    
    # 4개로(혹은 그 이상) 이어진 알파벳이 없으면 종료
    if t == False:
        break
    move()
    total += 1


print(total)
