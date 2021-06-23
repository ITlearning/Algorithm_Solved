def solution(strings, n):
    answer = []

    while True:
        t = True
        for i in range(len(strings)-1):
            if ord(strings[i][n]) > ord(strings[i+1][n]):
                t = False
                strings[i], strings[i+1] = strings[i+1], strings[i]
            elif ord(strings[i][n]) == ord(strings[i+1][n]):
                if strings[i] > strings[i+1]:
                    strings[i], strings[i+1] = strings[i+1], strings[i]
        if t:
            break

    
    answer = strings
    return answer 