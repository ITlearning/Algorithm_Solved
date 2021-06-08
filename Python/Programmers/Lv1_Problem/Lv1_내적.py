def solution(a, b):
    answer = 0
    tmp = 0
    for i,j in zip(a,b):
        tmp += int(i) * int(j)
    answer = tmp
    return answer