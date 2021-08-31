from itertools import combinations
def solution(orders, course):
    total = [] # 답 리스트
    
    for cur in course: # 입력받은 course의 수를 하나씩 돈다.
        answer = {}    # 조합을 입력받을 딕셔너리
        for item in range(len(orders)): # 입력받은 orders의 길이만큼 돈다.
            for i in list(combinations(orders[item],cur)): # course에서 입력한 숫자 만큼, 조합을 만들어본다.
                if "".join(sorted(i)) in answer: # answer 딕셔너리에 해당 key가 있다면
                    answer["".join(sorted(i))] += 1 # 주문된 횟수 추가
                else:                            # 해당 key가 없다면
                    answer["".join(sorted(i))] = 1 # 새로 생성
        
        if len(answer) != 0: # 입력받은 딕셔너리에 하나라도 들어가 있다면
            sanswer = sorted(answer.items(), reverse=True, key=lambda x: x[1]) # 주문받은 횟수 내림차순으로 정렬
            if sanswer[0][1] > 1: # 제일 큰 수가 2 이상이라면
                first = sanswer[0][1] # first에 제일 큰 수를 기준으로 설정
                #print(sanswer)
                total.append(sanswer[0][0]) # 답에 추가
                for i in sanswer[1:]:
                    if i[1] == first: # 주문받은 횟수가 기준으로 설정한 수와 같다면
                        total.append(i[0]) # 답에 추가
    total.sort() # 사전순 정렬
    return total

# 40분 소요

