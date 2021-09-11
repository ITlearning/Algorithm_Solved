from datetime import datetime
from math import ceil
def solution(fees, records):
    answer = {}
    total = {}
    stack = []
    an = {}
    defaultTime = fees[0]
    defaultPay = fees[1]
    defaultMin = fees[2]
    defaultWon = fees[3]

    for i in records:
        tmp = i.split()
        an[tmp[1]] = 0
        answer[tmp[1]] = defaultPay
        if tmp[1] not in total:
            total[tmp[1]] = [[tmp[0], tmp[2]]]
        else:
            total[tmp[1]].append([tmp[0], tmp[2]])
    
    #print(an)
    for value, name in zip(total.values(), total.keys()):
        for i in value:
            #print(i)
            if i[1] == 'IN':
                stack.append([i[0], name])  
            elif i[1] == 'OUT':
                if len(stack) != 0:
                    inTime = stack.pop()
                    #print(inTime)
                    inDate = datetime.strptime(inTime[0], '%H:%M')
                    outDate = datetime.strptime(i[0], '%H:%M')
                    inAndOut = outDate - inDate
                    if an[name] + inAndOut.seconds//60 > defaultTime:
                        an[name] += inAndOut.seconds//60
                    else:
                        an[name] += inAndOut.seconds//60
    
    for i in stack:
        #print(i)
        dayHour = datetime.strptime("23:59", '%H:%M')

        inDate = datetime.strptime(i[0], '%H:%M')
        inAndOut = dayHour - inDate
        #print(inAndOut.seconds // 60)
        if an[i[1]] + inAndOut.seconds // 60 > defaultTime:
            an[i[1]] += inAndOut.seconds // 60

    
    
    for name, time, in zip(an.keys(), an.values()):
        if time > defaultTime:
            answer[name] += ceil((time - defaultTime) / defaultMin) * defaultWon
    
    answer = sorted(answer.items())
    real_answer = []
    for i in answer:
        real_answer.append(i[1])
    return real_answer

print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))