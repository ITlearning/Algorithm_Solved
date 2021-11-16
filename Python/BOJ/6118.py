# 숨바꼭질
from collections import deque

n,m = map(int,input().split())
INF = int(1e9)
board = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

# 입력받은 숫자의 인덱스들 연결 시켜주기
for _ in range(m):
    A_i, B_i = map(int,input().split())
    # 입력받은 서로의 인덱스들에 서로의 숫자 넣어주기
    board[A_i].append(B_i)
    board[B_i].append(A_i)

# 거리 측정용 리스트
distance = [0]*(n + 1)

q = deque()
q.append(1)
distance[1] = 1  # 시작이니까 1로 시작

while q:
    x = q.popleft()
    for n in board[x]:
        # 방문하지 않은 곳이면
        if distance[n] == 0:
            # 방문해서 1 늘려줌
            distance[n] = distance[x] + 1
            q.append(n)

# 제일 큰 방문 거리
max_num = max(distance)

# 제일큰 숫자가 위치한 인덱스, 그 위치까지의 거리, 그 위치와 같은 거리의 원소들의 개수
print(distance.index(max_num), max_num - 1, distance.count(max_num))