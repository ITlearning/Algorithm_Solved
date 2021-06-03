# 숨바꼭질

# 양방향 통로로 이루어진 헛간
# 술래는 항상 1번부터 출발

import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n,m = map(int,input().split())
board = [[] for i in range(n+1)]
distance = [INF] * (n+1)
# 술래는 무조건 1에서 시작한다고 했으니 1로 초기화
start = 1
for _ in range(m):
    a,b = map(int,input().split())
    # 양방향 통로라고 했으니 양쪽 다 1로 입력
    board[a].append((b,1))
    board[b].append((a,1))

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: # 이미 방문했을 경우
            continue
        for i in board[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

# 최단 거리가 가장 먼 노드 (캐릭터가 숨을 헛간의 번호)
max_node = 0
# 도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1,n+1):
    if max_distance < distance[i]:
        max_node = i # 제일 먼 노드
        max_distance = distance[i] # 제일 먼 노드랑 떨어진 거리
        result = [max_node] # 먼 노드 리스트에 추가
    elif max_distance == distance[i] : # 제일 먼 노드와 떨어진 거리가 같을 경우
        result.append(i) # 같은거 찾으면 넣으라고 했으니까

# 제일 먼 노드,제일 먼 노드와 떨어진 거리, 먼 노드랑 떨어진 거리가 같은 노드 리스트 개수
print(max_node, max_distance, len(result)) 