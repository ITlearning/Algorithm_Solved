def solution(n, computers):
    answer = 0
    bfs = []
    dist = [0] *(n)
    
    while 0 in dist:
        x = dist.index(0)
        bfs.append(x)
        dist[x] = 1
        
        while bfs:
            node = bfs.pop(0)
            dist[node] = 1
            for i in range(n):
                if dist[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    dist[i] = 1
        answer += 1
    return answer