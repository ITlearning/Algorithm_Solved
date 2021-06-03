#플로이드 워셜 알고리즘
INF = int(1e9) # 무한으로 10억 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트 무한으로 전체 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
for a in range(1, n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아서 그 값으로 초기화 한다.
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행 Dab = min(Dab, Dak + Dkb)
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()

    # 시간 복잡도 O(N^3)