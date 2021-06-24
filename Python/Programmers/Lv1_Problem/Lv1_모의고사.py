def solution(answers):
    answer = []
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0,0,0]
    for i in range(len(answers)):
        if A[i%5] == answers[i]:
            cnt[0] += 1
        if B[i%8] == answers[i]:
            cnt[1] += 1
        if C[i%10] == answers[i]:
            cnt[2] += 1
            
            
    tmp = max(cnt)
    z = cnt.index(tmp)
    answer.append(z+1)
    for i in range(len(cnt)):
        if tmp == cnt[i]:
            if i != z:
                answer.append(i+1)
        
        
    return answer