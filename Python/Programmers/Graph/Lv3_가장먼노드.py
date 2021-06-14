from collections import deque

def solution(n, edge):
    graph = {}
    visited = [0] * n
    # 딕셔너리를 사용
    for i in edge:
        graph[i[0]] = graph.get(i[0], []) + [i[1]]
        graph[i[1]] = graph.get(i[1], []) + [i[0]]
        
    q = deque()
    q.append(1)
    visited[0] = 1
    
    while q:
        node = len(q)
        for i in range(node):
            cur = q.popleft()
            for c in graph[cur]:
                if visited[c-1] == 0:
                    visited[c-1] = 1
                    q.append(c)
    return node