def solution(N, stages):
    answer = []
    total = []
    copy = stages
    for i in range(1,N+1):
        tmp = []
        #print(len(copy))
        for j in range(len(copy)):
            #print(j)
            if i >= copy[j]:
                tmp.append(j)
        #print(tmp)
        #print(copy)
        if len(tmp) > 0:
            answer.append([len(tmp)/len(copy), i])
            for k in tmp[::-1]:
                #print(k)
                del copy[k]
        else:
            answer.append([0,i])
        
    answer.sort(reverse=True, key=lambda x: x[0])

    for i in answer:
        total.append(i[1])
    return total

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))

# 24분 09초