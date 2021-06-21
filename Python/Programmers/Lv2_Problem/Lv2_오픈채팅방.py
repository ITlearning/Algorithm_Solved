def solution(record):
    answer = []
    servers = []
    dic = {}
    for i in record:
        tmp = i.split(" ")
        if tmp[0] == "Leave":
            servers.append([tmp[1], "님이 나갔습니다."])
        elif tmp[0] == "Enter":
            dic[tmp[1]] = tmp[2]
            servers.append([tmp[1], "님이 들어왔습니다."])
        elif tmp[0] == "Change":
            dic[tmp[1]] = tmp[2]
    
    for server in servers:
        answer.append(dic[server[0]] + server[1])
    return answer