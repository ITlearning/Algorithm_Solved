from itertools import combinations

# 이분탐색 - 원하는 점수 이상으로 큰 수 탐색
def binary_search(point, item):
    start = 1
    end = len(item)

    answer = 0
    while start <= end:
        mid = (start + end) // 2
        # if mid > end:
        #     return answer
        if item[mid-1] >= point:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


def solution(infos, query):
    answer = [] # 답 리스트
    items = {}  # 각 상황들의 딕셔너리
    
    
    for i in range(len(infos)): # infos 크기만큼 돌린다.
        tmp = infos[i].split()  # infos[i] 의 문자열을 분리
        key = tmp[:-1]          # 분리한 문자열 중 key만 추출
        score = int(tmp[-1])    # 분리한 문자열 중 score만 추출
        for i in range(5):      # 5까지 돌면서
            for c in combinations(key, i):   # 총 16가지의 상황의 key 발급 후 적용
                tmp = "".join(c)             # 문자열로 바꿈
                if tmp in items:            # 딕셔너리에 해당 key값이 존재한다면
                    items[tmp].append(score) # 해당 딕셔너리 리스트에 점수 추가
                else:                        # 없다면
                    items[tmp] = [score]     # 새로운 딕셔너리 생성

                    
    # 각 딕셔너리의 점수 sort()
    # 여기서 안해주면 시간 초과 난다.
    # 따라서 먼저 해줘야함
    for key in items.keys():
        items[key].sort(reverse=True) # 이분탐색을 위해 반대로 정렬
        

    
    for j in range(len(query)):           # query 길이만큼 돌기
        q = query[j].replace("and", "")   # 해당 인덱스의 query에서 and 제거
        q = q.replace("-","")             # 해당 인덱스의 query에서 - 제거
        qq = q.split()                    # 해당 인덱스의 문자열 리스트로 분리(공백을 기준으로)
        plus = ''.join(qq[:-1])           # 분리한 문자열
        query[j] = [plus, int(qq[-1])]    # 기존의 query[i]에 새로운 리스트로 변경
        
    
    for i in query:           # 바꾼 query
        if i[0] in items:    # 딕셔너리에 해당하는 key값이 있다면
            tmp = items[i[0]] # query[0] : 딕셔너리 key query[1] = value
            p = binary_search(int(i[-1]),tmp) # 이분탐색 시작, 리턴값은 query 값보다 큰 숫자들의 개수
            answer.append(p) # 리턴값 입력
        else: # 만일 플레이어 리스트에 원하는 상태가 없다면
            answer.append(0) # 존재하지 않는 상황이니 0 입력

        

    return answer

infos = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(infos,query))


# 시간 셀 수 없음.