# DFS와 BFS
import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in range(1,n+1):
        if not visited[i] == False and graph[v][i] == 1:
            dfs(graph, i, visited)

n,m,v = map(int,input().split())
graph = [[]]
for _ in range(m):
    graph.append(list(map(int,input().split())))
visited = [False] * (m+1)

dfs(graph, v, visited)