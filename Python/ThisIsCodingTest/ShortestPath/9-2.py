# 다익스트라 알고리즘 - 개선된 구현 방법
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
 
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF :
        print("INFINITY")
    else:
        print(distance[i])


# 시간 복잡도 O(ElogV)이다.