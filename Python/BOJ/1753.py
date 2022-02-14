# 최단경로
import heapq
import sys
input = sys.stdin.readline
# v : 정점의 개수
# e : 간선의 개수
# start : 시작 노드
v,e = map(int,input().split())
start = int(input())
INF = int(1e9)

graph = [[] for _ in range(v+1)]
distance = [INF for _ in range(v+1)]

for _ in range(e):
    a,b, num = map(int,input().split())
    graph[a].append([b,num])

# 다익스트라 실행
def djikstra(start):
    q = []
    # 초기설정
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 거리에 표시된 길이와 현재 위치 뽑기
        dist, now = heapq.heappop(q)
        
        # 지금 위치의 기록된 거리가 뽑은 거리보다 작으면
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            # for문 돌려서 지금 거리보다 적은 수의 거리가 나오면
            if cost < distance[i[0]]:
                # 갱신하고 우선순위 큐에 넣기
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

djikstra(start)

# 출력
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])