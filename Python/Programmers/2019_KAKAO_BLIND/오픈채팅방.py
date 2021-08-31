def solution(record):
    answer = []
    result = []
    total = {}
    for co in record:
        tmp = co.split()
        if tmp[0] == 'Enter':
            total[tmp[1]] = tmp[2]
            answer.append([tmp[1], "I"])
        elif tmp[0] == 'Leave':
            answer.append([tmp[1], "L"])
        elif tmp[0] == 'Change':
            total[tmp[1]] = tmp[2]

    for i in answer:
        if i[1] == "I":
            result.append(total[i[0]]+"님이 들어왔습니다.")
        elif i[1] == "L":
            result.append(total[i[0]]+"님이 나갔습니다.")


    return result

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))

# 17분 37초 15