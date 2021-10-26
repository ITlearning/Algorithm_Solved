# 인구 이동
from collections import deque
n,l,r = map(int,input().split())

dx = [0,-1,0,1]
dy = [-1,0,1,0]
board = []

for i in range(n):
    board.append(list(map(int,input().split())))

def bfs(i,j):
    dist[i][j] = 1
    q = deque()
    q.append([i,j])
    tmp = []
    tmp.append([i,j])
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == 0:
                if l <= abs(board[nx][ny] - board[x][y]) <= r: # L명 이상 R명 이하면 추가
                    dist[nx][ny] = 1
                    q.append([nx,ny]) # 얘는 돌릴때 덱
                    tmp.append([nx,ny]) # 얘는 조건에 부합하는 좌표 저장
    return tmp # 모은 좌표들 리턴

cnt = 0

while True:
    dist = [[0 for _ in range(n)] for _ in range(n)] # 방문여부 리스트
    t = False
    for i in range(n):
        for j in range(n):
            if dist[i][j] == 0: # 방문 안했으면
                result = bfs(i,j) # bfs돌리기
                if len(result) > 1:
                    t = True
                    num = sum(board[x][y] for x,y in result) // len(result) # 리턴받은 좌표들을 더해서 길이와 나누기
                    for x,y in result: # 그리고 나온 수를 부합하는 좌표들에 대입
                        board[x][y] = num
    if t == False: # 더이상 바꿀게 없으면 종료
        break
    cnt += 1 # 그게 아니라면 카운트 증가

print(cnt)