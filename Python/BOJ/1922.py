# 네트워크 연결

# 최소 스패닝 트리
# 그래프에서 그래프의 모든 정점을 연결하되,
# 사이클이 존재하지 않도록 모든 정점을 간선으로 연결하는 것을 의미

# 이때, 간선의 가중치 합을 최소로 하며 연결해야 한다.

# 크루스칼 알고리즘

# 모든 간선에 대해 가장 가중치가 작은 간선부터 연결해주면서
# 최소 스패닝 트리를 만들어 나가는 알고리즘

# 이때, 작은 간선이라도 사이클이 만들어지면 무시해야 한다.

import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])

    return parent[x]

def union(x,y):
    x,y = find(x), find(y)
    parent[x] = y

n = int(input())
m = int(input())

board = [list(map(int,input().split())) for _ in range(m)]
board = sorted(board, key=lambda x : x[2])

parent = [i for i in range(0, n+2)]

answer = 0

for i in board:
    start, end, width = i
    # 사이클이면
    if find(start) == find(end):
        continue
    else:
        answer += width
        union(start, end)

print(answer)