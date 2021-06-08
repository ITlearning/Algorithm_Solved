def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for a,b in zip(participant,completion):
        if a != b:
            return a
    
    answer += str(participant[-1])
    return answer