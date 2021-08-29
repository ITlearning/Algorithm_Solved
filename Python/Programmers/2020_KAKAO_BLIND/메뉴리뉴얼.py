from itertools import combinations
def solution(orders, course):
    total = []
    
    for cur in course:
        answer = {}
        for item in range(len(orders)):
            for i in list(combinations(orders[item],cur)):
                if "".join(sorted(i)) in answer:
                    answer["".join(sorted(i))] += 1
                else:
                    answer["".join(sorted(i))] = 1
        if len(answer) != 0:
            sanswer = sorted(answer.items(), reverse=True, key=lambda x: x[1])
            if sanswer[0][1] > 1:
                first = sanswer[0][1]
                #print(sanswer)
                total.append(sanswer[0][0])
                for i in sanswer[1:]:
                    if i[1] == first:
                        total.append(i[0])
    total.sort()
    return total

# 40분 소요