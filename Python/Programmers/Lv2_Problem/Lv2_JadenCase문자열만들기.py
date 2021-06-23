def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i].isalpha() and s[i-1] == " " or i == 0:
            answer += s[i].upper()
        elif s[i].isalpha() and (s[i-1].isalpha() or not s[i-1].isalpha()):
            answer += s[i].lower()
        else:
            answer += s[i]
        
    
    return answer