
def solution(s):
    answer = []
    stack = []
    mid = len(s) // 2
    #print(mid)
    i = 1

    if len(s) <= 1:
        answer.append(s)

    while i <= mid:
        total = ""
        #print(i) 
        for index in range(0,len(s)+1, i):
            #print(s[index:index+i])
            if len(stack) == 0:
                stack.append(s[index:index+i])
            elif stack[-1] == s[index:index+i]:
                stack.append(s[index:index+i])
                
            else:
                #print(stack)
                if len(stack) >= 2:
                    total += str(len(stack))+stack[-1]
                    #print(total)
                else:
                    if len(stack) != 0:
                        total += stack[-1]
                    #print(total)
                stack.clear()
                stack.append(s[index:index+i])
        #print(index)
        if index < len(s):
            total += s[index:]
            stack.clear()
        #print(total)   
        answer.append(total)
        
        i += 1
    #print(total)
    answer.sort(key=len)
    return len(answer[0])

# 38분 22초

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("xababcdcdababcdcd"))
print(solution("a"))