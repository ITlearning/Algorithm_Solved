def solution(N, stages):
    answer = []
    people = len(stages)
    tmp = []
    tt = []
    for i in range(1,N+1):
        not_goal = 0
        for stage in stages:
            if i <= stage <= i:
                not_goal += 1
        if not_goal == 0:
            tmp.append([i,not_goal])
        else:
            answer.append([i,people/not_goal])
        people -= not_goal
        
        answer.sort(key=lambda x: x[1])
        tmp.sort()
        
    for i in answer:
        tt.append(i[0])
    for i in tmp:
        tt.append(i[0])
    return tt