# <문제 - 전보>
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())
board = [[] for i in range(n+1)] # 각 노드에 연결되어있는 노드에 대한 정보 담는 리스트
dis = [INF] * (n+1) # 최단 거리 테이블

for _ in range(m):
    a,b,c = map(int, input().split())
    board[a].append((b,c))


def dijkstra(start):
   # m = 0
    #cnt = 0
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in board[now] :
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                #cnt += 1
                #m = max(m, cost)

    #return cnt, m
        
dijkstra(start)

count = 0
max_dis = 0
for d in dis:
    if d != INF:
        count += 1
        max_dis = max(max_dis, d)

print(count-1, max_dis)