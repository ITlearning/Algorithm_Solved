# 비밀번호 발음하기
text_list = []
vowel = ["a", "e", "i", "o", "u"]  # 모음
double_text = ["ee", "oo"]         # 연속 허용 단어


while True:
    text = input()
    # end 입력시 종료
    if text == "end":
        break
    # end 입력 받기 전까지 단어 입력받기
    text_list.append(text)

# 입력받은 단어 돌면서
for text in text_list:
    vowel_cnt = 0   # 1. 모음 하나를 반드시 포함하여야 한다.
    v_cnt = 0 # 모음이 3개 혹은 
    c_cnt = 0 # 자음이 3개 연속으로 오면 안된다.
    text_stack = [] # 단어 하나에서 확인한 알파벳들 
    twice = False # 같은 알파벳이 두개 연속 이어질 경우 체크용 Bool
    for index in range(len(text)):
        # 모음이든 자음이든 3개 연속 됐을 경우 종료
        if v_cnt >= 3 or c_cnt >= 3:
            break
        # 모음일 경우
        if text[index] in vowel:
            # 만일 자음 카운트가 됐을 경우
            if c_cnt != 0:
                # 초기화
                c_cnt = 0
            
            # 모음의 최소 수를 세기 위한 카운트
            vowel_cnt += 1
            # 모음 카운트
            v_cnt += 1
        else:  # 자음일 경우
            # 만일 모음 카운트가 됐을 경우
            if v_cnt != 0:
                # 초기화
                v_cnt = 0
            # 자음 카운트
            c_cnt += 1

        # 연속 알파벳 체크
        if len(text_stack) >= 1 and text_stack[-1] == text[index]:
            # 만일 연속 허용 단어일 경우
            if "".join(text_stack[-1]+text[index]) in double_text:
                # 지나가기
                continue
            else:  # 불가능 단어일 경우
                twice = True  # Bool True 설정하고 종료
                break
        # 조건문에 관계 없이 알파벳 저장
        text_stack.append(text[index])
    
    # 모든 제한 조건 중 하나라도 걸리면 true
    if v_cnt >= 3 or c_cnt >= 3 or vowel_cnt == 0 or twice:
        print("<"+text+"> is not acceptable.")
    else:  # 아닐경우 false
        print("<"+text+"> is acceptable.")
        