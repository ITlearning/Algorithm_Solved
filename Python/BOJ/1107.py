# 리모컨
import sys
input = sys.stdin.readline

want_channel = int(input())
remote_controller = [str(i) for i in range(10)]

m = int(input())

if m != 0:
    remove_button = list(map(int,input().split()))
    
    for remove in remove_button:
        remote_controller.remove(str(remove))

cnt = abs(100-want_channel) # -,+ 버튼만으로 움직일 수 있는 채널 횟수를 먼저 따진다.

for k in range(1000000): # 최대 500,000으로 제한되어 있는데, 마이너스의 경우와 플러스의 경우를 다 따져봐야하기에 2배 숫자
    num = str(k)
    for i in range(len(num)):
        if num[i] not in remote_controller:
            break
        if i == len(num)-1:
            cnt = min(cnt, abs(want_channel - k) + len(num))

print(cnt)
