def solution(s):
    answer = -1
    tmp = []
    for i in s:
        tmp.append(i)
        if len(tmp) >= 2:
            if tmp[-2] == tmp[-1]:
                tmp.pop()
                tmp.pop()
    if len(tmp) == 0:
        answer = 1
    else:
        answer = 0
    return answer