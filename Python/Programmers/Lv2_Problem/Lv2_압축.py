def solution(msg):
    answer = []
    al = {}
    cnt = 1
    for i in range(65, 91):
        al[chr(i)] = cnt
        cnt += 1
        
    w,c = 0,0
    while True:
        c += 1
        if c == len(msg):
            answer.append(al[msg[w:c]])
            break
        if msg[w:c+1] not in al:
            al[msg[w:c+1]] = len(al)+1
            answer.append(al[msg[w:c]])
            w = c
    return answer