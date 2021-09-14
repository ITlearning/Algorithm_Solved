def solution(N, stages):
    answer = []
    total = []
    # stage 복사
    copy = stages

    # 1부터 돌면서
    for i in range(1,N+1):
        tmp = []
        for j in range(len(copy)):
            # 만일 지금 스테이지보다 같거나 적은 스테이지라면
            if i >= copy[j]:
                # 추가
                tmp.append(j)
        # tmp에 하나라도 존재하면
        if len(tmp) > 0:
            # answer 리스트에 실패율과 해당 번호 같이 추가
            answer.append([len(tmp)/len(copy), i])
            
            # 실패율 계산한 것들 제거
            for k in tmp[::-1]:
                del copy[k]
        else:
            # 그게 아니면 확률이 0이니 0과 함께 스테이지 추가
            answer.append([0,i])
    
    # 작은번호 순으로 정렬
    answer.sort(reverse=True, key=lambda x: x[0])

    # total에 답 입력
    for i in answer:
        total.append(i[1])

    return total

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))

# 24분 09초