# 3. 올바른 괄호 문자열인지 체크
def right(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0:
            return False
    return True

# 4-4. 괄호 바꾸기
def reverse(s):
    tmp = ''
    for i in s:
        if i == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp


def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if len(p) == 0:
        return ""
    
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(': # ( 일 경우 +1
            cnt += 1
        else:           # ) 일경우 -1
            cnt -= 1
        if cnt == 0: # 이렇게 하다가 0이 될 경우는 올바른 괄호 문자이기 때문에
            u = p[:i+1] # U
            v = p[i+1:] # V 로 나눠준다.
            break
    if right(u): # 그리고선 올바른 괄호 문자열인지 체크
        # 3 작업 
        return u + solution(v) # 맞을 경우 u에 수행한 결과를 이어 붙인 후 반환
    else: 
        # 4-1 ~ 4-5 작업
        return '(' + solution(v) + ')' + reverse(u[1:-1]) # 맞지 않을 경우 '(' + solution(v) + ')' 후에 문자열의 괄호 방향을 뒤집은 reverse() 도 더한다.

solution("(()())()")

# 재귀를 잘 모름..
# 1시간 소요..