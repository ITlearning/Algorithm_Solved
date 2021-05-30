# 문자열 압축

def solution(s):
    length = []
    result = ""
    
    if len(s) == 1:
        return 1
    
    for i in range(1,len(s)//2 + 1) :
        cnt = 1
        tempStr = s[:i]
        for j in range(i, len(s), i):
            if s[j:j+i] == tempStr:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                result += str(cnt) + tempStr
                tempStr = s[j:j+i]
                cnt = 1
        if cnt == 1:
            cnt = ""
        result += str(cnt) + tempStr
        length.append(len(result))
        result = ""
        
    return min(length)

    # 출처 - https://url.kr/okrnv7 