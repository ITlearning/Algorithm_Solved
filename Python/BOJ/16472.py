# 고냥이
n = int(input())

text = input()
answer = {} # 입력받은 문자들의 개수를 셀 수 있는 딕셔너리
start = 0 
end = 0
#print(answer)
total = 0
# 투 포인터 사용
while start <= end:
    # 오른쪽 포인터가 text의 길이만큼 이동했을 경우 종료
    if end >= len(text):
        break

    # 딕셔너리에 해당 인덱스의 글자가 있을 경우
    if text[end] in answer:
        answer[text[end]] += 1
    else: # 없을 경우
        answer[text[end]] = 1
    
    print(answer)

    # 알파벳 숫자가 허용치보다 커졌을 경우
    while len(answer) > n:
        #print("와일문")
        answer[text[start]] -= 1
        
        # 알파벳의 개수가 0일 경우, 제거
        if answer[text[start]] == 0:
            del answer[text[start]]
        #print(answer)
        start += 1
    #print("턴 종료")
    end += 1
    # 답은 투 포인터의 차이가 제일 클 경우
    total = max(total, end - start )
    
    #print(total)
    

# 답 도출
print(total)
