def solution(s):
    answer = []     # 모든 경우의 문자열들을 저장할 answer리스트
    mid = len(s)//2 # 문자열 비교는 중간값까지만 (크기의 반)
    
    if len(s) == 1: # 만일 문자열의 길이가 1일 경우
        answer.append(s) # 그냥 추가
    
    for i in range(1,mid+1): # 나눈 문자열 길이를 1부터 중간값까지 돌린다.
        start = 0            # 슬라이싱 시작점
        cnt = 0              # 중복된 글자 수 카운트
        total = ""           # 정해진 글자 수 대로 만들어진 문자열
        for cur in range(0,len(s)+1, i): # range(0,0,0) 로 나눠지는 구간을 설정
            if s[start:cur] == s[start+i:cur+i]: # 현재 선택된 문자열과 다음 문자열이 같을경우
                cnt += 1                 # 카운트 해줌
            else:                        # 그게 아니면
                if cnt > 1:              # 만약 카운트가 1 이상 이라면(연속된 글자가 하나 이상)
                    total += str(cnt) + s[start:cur] # 카운트와 같이 연속된 문자열 추가
                else:                     # 그게 아니면
                    total += s[start:cur] # 그냥 문자열만 추가
                cnt = 1 # 카운트 초기화
            start = cur # 현재 문자열 확인 끝났으니까 다음 문자열 확인하기 위해서 슬라이싱 시작점 업데이트
            
        # for문을 돌았는데 나눠주는 수가 인덱스보다 커서 못 넘어간 경우    
        # 그러면 인덱스보다 적은 상태로 for문이 종료됐을것이다.
        if cur < len(s): # 만일 그렇다면
            total += s[cur:len(s)] # 나머지 있던 문자열들도 total에 입력해준다.
        answer.append(total) # 그리고 answer리스트에 추가
        
        total = "" # total 초기화
        
    # 문자열 길이를 기준으로 오름차순 정렬
    answer.sort(key=lambda x : len(x))        
    return len(answer[0]) # 가장 짧은 길이 출력