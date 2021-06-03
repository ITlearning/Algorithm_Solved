# 화성 탐사

# N X N 크기의 맵이 주어졌을 때, 맵의 각 위치(칸)를 '노드'로 보고,
# 상하좌우로 모든 노드가 연결되어 있다고 보면 된다.

# 또한 N의 최대 크기가 125로 작게 보이지만,
# 2차원 공간이기에 최대 10,000을 넘길 수 있기 때문에
# 플로이드 워셜 알고리즘은 못 쓴다 (ㅠㅠ)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

# 이게 아까 칸으로 생각하라고 했으니까 일단 최소로 움직이는
# 값을 따지고 싶다면 힙으로 모든 값을 왔다갔다 해서
# 값을 따지고 난 뒤에 출력해내는 형식이어야 한다.
# 따라서 상,하,좌,우 로 이동할 수 있게 리스트를 작성해놓은 모습
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for tc in range(int(input())):
    # 노드의 개수
    n = int(input())
    board = []
    # 맵 전체 입력받기
    for i in range(n):
        board.append(list(map(int,input().split())))
    # 최단 거리 테이블 모두 초기화
    distance = [[INF] * (n) for _ in range(n)]

    x,y = 0,0 # 시작 위치
    q = [(board[x][y], x, y)]
    distance[x][y] = board[x][y]

    # 다익스트라
    while q:
        dist, x,y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        # 상하좌우 움직여본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            cost = dist + board[nx][ny]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost,nx,ny))

print(distance[n - 1][n - 1])