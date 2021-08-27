

def solution(p):
    answer = ""
    total = []
    # 1. 입력이 빈 문자열의 경우, 빈 문자열을 반환합니다
    if len(p) == 0:
        return ""
    
    for i in range(len(p)):
        total.append(p[i])
        

    return total

p = "()))((()"
t = solution(p)

print(t)
