# 고냥이
n = int(input())

text = input()
answer = {}
start = 0
end = 0
#print(answer)
total = 0
while start <= end:
    if end >= len(text):
        break

    if text[end] in answer:
        answer[text[end]] += 1
    else:
        answer[text[end]] = 1
    #print(answer)
    while len(answer) > n:
        #print("와일문")
        answer[text[start]] -= 1
        
        if answer[text[start]] == 0:
            del answer[text[start]]
        print(answer)
        start += 1
    #print("턴 종료")
    end += 1
    total = max(total, end - start )
    
    #print(total)
    

    
print(total)
