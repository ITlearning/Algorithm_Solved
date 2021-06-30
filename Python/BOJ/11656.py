# 접미사 배열
import sys
input = sys.stdin.readline
S = input().rstrip()
answer = []

for i in range(0,len(S)):
    answer.append(S[i:len(S)])
if len(answer) != 0:
    answer.sort()
    for i in answer:
        print(i)