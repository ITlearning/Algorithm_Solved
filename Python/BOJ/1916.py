# 최소비용 구하기
import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
inf = 100000000

# 입력받을 그래프와, 거리 측정용 distance
graph = [[] for _ in range(n+1)]
distance = [inf for _ in range(n+1)]

# 1. 입력받기
for _ in range(m):
    a,b, dist = map(int,input().split())
    graph[a].append([b, dist]) 

# 시작과 끝 입력받기
start, end = map(int,input().split())

# 2. 다익스트라 돌리기
def dijkstra(start):
    # 값 초기화 (우선순위 사용)
    q = []
    distance[start] = 0
    # 거리와 시작위치 저장
    heapq.heappush(q, [0, start])
    
    # q 빌때까지 돌리기
    while q:
        dist, now = heapq.heappop(q)
        # 지금 위치의 거리가 저장된(갱신된) 거리보다 크다면
        if distance[now] < dist:
            continue

        # 지금 위치의 그래프 리스트 뽑아와서 비교하기
        for move, cost in graph[now]:
            # 일단 거리 먼저 더해서 사용해보기
            tmp = dist + cost
            # 그 거리가 지금 저장된(갱신된) 거리보다 작으면
            if tmp < distance[move]:
                # 거리 갱신해주고
                distance[move] = tmp
                # 우선순위에 넣어주기
                heapq.heappush(q, (tmp, move))

dijkstra(start)
print(distance[end])