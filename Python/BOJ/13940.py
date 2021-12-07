# A와 B
from collections import deque
s = input()
t = input()

# 우리가 만들어야 할 글자를 조건과 반대로 해가면서
# 답을 찾아냄
while len(t) >= len(s):
    # 만약에 시작한 글자와 같아지면
    # 1을 출력하고 종료
    if t == s:
        print(1)
        exit()
    
    # 문자열의 뒤에 A를 추가한다. -> 문자열의 뒤가 A 라면 A를 지운다.
    if t[-1] == "A":
        t = t[0:-1]
    # 문자열을 뒤집고 뒤에 B를 추가한다. -> 문자열의 뒤가 B라면 B를 지우고 뒤집는다.
    elif t[-1] == "B":
        t = t[0:-1]
        t = t[::-1]

# while문을 다 돌았는데도 종료가 안됐다면 0을 출력
print(0)