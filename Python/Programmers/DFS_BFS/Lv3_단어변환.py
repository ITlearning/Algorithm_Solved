answer = 0

def dfs(begin, target,words, visited):
    global answer
    stacks = [begin]
    while stacks:
        stack = stacks.pop()
        
        if stack == target:
            return answer
        
        for i in range(0,len(words)):
            # 이게 핵심인데 이해가 안간다..
            if len([k for k in range(0,len(words[i])) if words[i][k] != stack[k]]) == 1:
                if visited[i] != 0:
                    continue
                
                visited[i] = 1
                
                stacks.append(words[i])
                
        answer += 1

def solution(begin, target, words):
    global answer
    
    if target not in words:
        return 0
    
    visited = [0 for i in words]
    
    dfs(begin, target, words, visited)
    return answer