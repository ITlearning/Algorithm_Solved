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

# 4. 괄호 바꾸기
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
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    if right(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse(u[1:-1])