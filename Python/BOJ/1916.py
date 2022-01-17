# 최소비용 구하기
import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
inf = 100000000
    
graph = [[] for _ in range(n+1)]
distance = [inf for _ in range(n+1)]

for _ in range(m):
    a,b, dist = map(int,input().split())
    graph[a].append([b, dist]) 

start, end = map(int,input().split())

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, [0, start])
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for move, cost in graph[now]:
            tmp = dist + cost
            if tmp < distance[move]:
                distance[move] = tmp
                heapq.heappush(q, (tmp, move))

dijkstra(start)
print(distance[end])