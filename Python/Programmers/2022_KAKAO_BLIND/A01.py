def solution(id_list, report, k):
    answer = []
    total = {}
    cnt = {}
    for i in id_list:
        total[i] = []
        cnt[i] = 0

    for j in report:
        tmp = j.split()
        if tmp[1] not in total[tmp[0]]:
            total[tmp[0]].append(tmp[1])
    
    for i in total.values():
        for j in i:
            cnt[j] += 1

    for i in total.values():
        t = 0
        for j in i:
            if cnt[j] >= k:
                t += 1
        #print(t)
        answer.append(t)

    #print(total)


    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))