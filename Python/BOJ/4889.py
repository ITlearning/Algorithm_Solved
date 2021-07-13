# 안정적인 문자열
import sys
input = sys.stdin.readline
cnt = 1 # 순서 카운트 변수


while True:
    s = [] # 스택역할 리스트
    text = input().rstrip()
    change = 0 # 바꾼 수
    
    # 일단 먼저 불안정한 것만 뽑아서 저장한다
    for i in text:       # 입력받은 괄호 하나씩 돌면서
        if i == "{":     # 만일 괄호가 { 일 경우
            s.append(i)  # 일단 스택에 추가
        elif i == "}":   # 반대로 } 일 경우
            if len(s) == 0 or s[-1] != "{": # 스택이 비어있거나, 마지막으로 넣은게 반대괄호가 아닐 경우
                s.append(i) # 추가
            else: # 그게 아니고 짝이 맞는 경우
                s.pop() # 짝 맞춰진거니 빼줌
        else: # 괄호 이외의 것이 들어오면 프로그램 종료
            exit(0)

    #불안정한 것들만 처리
    while s:        # 안정적이지 않은 괄호들의 스택
        tmp = s[-1] # 제일 마지막에 넣은 것
        s.pop()     # 하나 빼주고
        if s[-1] != tmp: # 마지막에 넣은게 그 전 스택이랑 다를 경우 ex) }{
            change += 2  # 2 추가
        else: # 그게 아니고 같을 경우 ex) {{ , }}
            change += 1  # 1 추가
        s.pop() # 비교가 끝났으니 마저 pop 해줌
    
    print(cnt,". ",change, sep='') # 결과 출력
    cnt += 1