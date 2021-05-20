# 에디터

import sys
        # sys.stdin.readline() - 문자열 입력 받기
        # 이렇게 해야 시간초과가 발생하지 않는다.
        # rstrip() 문자열 오른쪽에서부터 제거합니다.
strings = sys.stdin.readline().rstrip()
commands = int(sys.stdin.readline().rstrip())
left = []
right = []

for i in range(len(strings)) :
    left.append(strings[i])

for i in range(commands) :
    commands = sys.stdin.readline().rstrip().split()
    if commands[0] == "P" :
        left.append(commands[1])
    elif commands[0] == 'L' :
        if len(left) :
            move = left.pop()
            right.append(move)
    elif commands[0] == 'D' :
        if len(right) :
            move = right.pop()
            left.append(move)
    else :
        if len(left) :
            left.pop()

print(''.join(left+right[::-1]))