def solution(d, budget):
    answer = 0
    d.sort()
    money = 0
    cnt = 0
    for i in d:
        money += i
        if money > budget:
            break
        cnt += 1
        
    return cnt