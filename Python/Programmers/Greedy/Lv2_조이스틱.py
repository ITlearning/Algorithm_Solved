def solution(name):
    # 리스트로 이름을 조각조각 내기
    name = list(name)
    i = 0
    answer = 0
    
    while True:
        # name의 한글자 한글자를 기준으로 A 에서 부터 가까우면 왼쪽 값을, Z에서 부터 가까우면 오른쪽 값을 채택
        answer += min(ord(name[i]) - ord('A'), ord('Z')- ord(name[i])+1)
        name[i] = 'A'
        
        # 만일 위에 설정해준 A의 개수가 본래 길이와 같아질경우 턴 종료
        if name.count('A') == len(name) : return answer 
        
        left, right = 1,1
        # 만약 위치한 곳이 이미 갔던 곳이라면 A로 되어있을 테니, 계속 더해줘서 인덱스를 바꿔주고
        # 아니라면 그쪽부터 찾아야 하니 중지
        for l in range(1,len(name)):
            if name[i-l] == 'A': left += 1
            else : break
                
        for r in range(1, len(name)):
            if name[i+r] == 'A' : right += 1
            else : break
                
        if left < right:
            answer += left
            i -= left
        else:
            answer += right
            i += right
    return answer