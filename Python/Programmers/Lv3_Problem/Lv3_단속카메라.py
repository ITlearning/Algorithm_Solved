def solution(routes):
    answer = 0
    routes.sort()
    s = routes[0][1]
    routes.pop(0)
    answer += 1
    print(routes)
    for i in routes:
        if i[0] <= s:
            s = min(s,i[1])
        else:
            s = i[1]
            answer += 1
    return answer