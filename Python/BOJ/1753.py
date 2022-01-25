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


def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])


djikstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])