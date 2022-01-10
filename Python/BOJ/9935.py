# 문자열 폭발
text = input()
match_text = input().rstrip()
stack = []

for i in text:
    # stack에 글자 하나 추가
    stack.append(i)
    # 추가한 글자와 찾아야할 단어 마지막 글자가 같고, 현재 모아진 문자 중 찾아야할 글자의 길이만큼 대조해서 찾아야할 글자라면
    if i == match_text[-1] and "".join(stack[-len(match_text):]) == match_text:
        for _ in range(len(match_text)):
            # 찾아야할 글자만큼 뽑아내기
            stack.pop()

# 그렇게 해서 stack이 남아있다면
if stack:
    # 출력
    print("".join(stack))
else:
    # 남아있지 않으면 출력
    print("FRULA")