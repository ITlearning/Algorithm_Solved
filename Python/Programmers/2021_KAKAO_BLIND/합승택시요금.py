import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(n,start, graph, distance,index):
    q = []
    distance = [INF] * (n+1)
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
                heapq.heappush(q, (cost,i[0]))
    return distance[index]

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for x,y,z in fares:
        graph[x].append([y,z])
        graph[y].append([x,z])
    
    cost = dijkstra(n,s,graph, distance,a) + dijkstra(n,s,graph, distance,b)

    for i in range(1, n+1):
        if s != i:
            cost = min(cost, (dijkstra(n,s,graph, distance,i) + dijkstra(n,i,graph, distance,a) + dijkstra(n,i,graph, distance,b)))
    return cost

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6,
        [[2, 6, 6], 
        [6, 3, 7], 
        [4, 6, 7], 
        [6, 5, 11], 
        [2, 5, 12], 
        [5, 3, 20], 
        [2, 4, 8], 
        [4, 3, 9]]))


# 2 시간 24분 02초