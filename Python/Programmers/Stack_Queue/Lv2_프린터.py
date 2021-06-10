def solution(priorities, location):
    d = []
    cnt = 0 # 각 프린터할 것들의 인덱스
    tmp = 0 # 최댓값 변수
    for i in priorities:
        d.append((cnt, i))
        cnt += 1
    
    result = 0 # 출력된 순서
    while len(d) != 0: # d의 원소들이 없어질때까지 돌아감
        tmp = 0
        for i in d:
            if tmp < i[1]:
                tmp = i[1]
        check = d[0]
        if check[1] < tmp:
            d.pop(0)
            d.append(check)
        else:
            result += 1
            if check[0] == location: # 원했던 로케이션에 맞는 인덱스가 출력 될 시 순서 리턴
                return result
            d.pop(0) # 그게 아니면 순서 증가시키고 pop()