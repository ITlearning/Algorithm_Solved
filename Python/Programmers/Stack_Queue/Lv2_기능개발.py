from collections import deque
def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while len(progresses):
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
            
        if cnt >= 1:
            answer.append(cnt)
        
    return answer