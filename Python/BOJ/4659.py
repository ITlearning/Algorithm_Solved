# 비밀번호 발음하기
text_list = []
vowel = ["a", "e", "i", "o", "u"]
double_text = ["ee", "oo"]


while True:
    text = input()

    if text == "end":
        break

    text_list.append(text)

for text in text_list:
    vowel_cnt = 0   # 1. 모음 하나를 반드시 포함하여야 한다.
    v_cnt = 0 # 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
    c_cnt = 0
    text_stack = []
    twice = False
    for index in range(len(text)):
        if v_cnt >= 3 or c_cnt >= 3:
            break

        if text[index] in vowel:
            if c_cnt != 0:
                c_cnt = 0
            vowel_cnt += 1
            v_cnt += 1
        else:
            if v_cnt != 0:
                v_cnt = 0
            c_cnt += 1

        if len(text_stack) >= 1 and text_stack[-1] == text[index]:
            if "".join(text_stack[-1]+text[index]) in double_text:
                continue
            else:
                twice = True
                break
        text_stack.append(text[index])
    
    if v_cnt >= 3 or c_cnt >= 3 or vowel_cnt == 0 or twice:
        print("<"+text+"> is not acceptable.")
    else:
        print("<"+text+"> is acceptable.")
        