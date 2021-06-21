def solution(numbers):
    answer = []
    numbers.sort()
    num = 0
    while num != len(numbers):
        for i in range(num+1,len(numbers)):
            if numbers[num] + numbers[i] not in answer:
                answer.append(numbers[num] + numbers[i])
        num += 1
    answer.sort()
    return answer