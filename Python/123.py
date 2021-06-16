from collections import deque
import sys

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 1
    while q:
        node = q.popleft()
        for n in graph[node]:
            if check[n] == 0:
                check[n] = 1
                q.append(n)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[v].append(u)
res = []
for i in range(1, N+1):
    check = [0]*(N+1)
    bfs(i)
    res.append(check.count(1))
m = max(res)
for i in range(N):
    if res[i] == m:
        print(i+1, end=' ')
print()