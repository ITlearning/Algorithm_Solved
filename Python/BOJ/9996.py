# 한국이 그리울 땐 서버에 접속하지
import sys
input = sys.stdin.readline

N = int(input())

target = input().rstrip()
target_split = target.split('*')
S = []
for i in range(N):
    S.append(input().rstrip())
T = True
for text in S:
    cnt = 0
    if not text.startswith(target_split[0]):
        T = False
    else:
        cnt += len(target_split[0])
    if not text.endswith(target_split[1]):
        T = False
    else:
        cnt += len(target_split[1])
    
    if cnt > len(text):
        print("NE")
        T = True
        continue
    
    if T:
        print("DA")
    else:
        print("NE")
    T = True