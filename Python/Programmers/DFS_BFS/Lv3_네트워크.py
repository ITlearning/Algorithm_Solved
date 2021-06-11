def dfs(i, computers, dist):
    if dist[i]:
        return 0
    
    dist[i] = True
    for j in range(len(computers[i])):
        if computers[i][j] == 1:
            dfs(j, computers, dist)
            
    return 1

def solution(n, computers):
    answer = 0
    dist = [False for i in range(n)] 

    for a in range(n):
        if not dist[a]:
            answer += dfs(a, computers, dist)  
    
    return answer