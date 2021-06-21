# 재귀함수가 뭔가요?
import sys
input = sys.stdin.readline
t = int(input())

def c(n):
    for _ in range(n):
        print("____",end='')

def func(s,t):
    c(s)
    print("재귀함수가 뭔가요?")
    if s == t:
        c(s)
        print("재귀함수는 자기 자신을 호출하는 함수라네")
        c(s)
        print("라고 답변하였지.")
    else:
        c(s)
        print("잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        c(s)
        print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        c(s)
        print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.")
        func(s+1,t)
        c(s)
        print("라고 답변하였지.")

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
func(0,t)