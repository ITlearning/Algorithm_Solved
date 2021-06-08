def solution(absolutes, signs):
    answer = 123456789
    tmp = []
    for a,b in zip(absolutes, signs):
        if b == False:
            tmp.append(-int(a))
        else:
            tmp.append(int(a))
            
    answer = sum(tmp)
    return answer