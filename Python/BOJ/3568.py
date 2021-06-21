# iSharp
import sys
input = sys.stdin.readline
text = input().rstrip()
text_list = text.split(' ')
# 기본 변수형
function = text_list[0]
del text_list[0]
for i in text_list:
    # 두개 제거
    i = i.replace(",", '').replace(";",'')
    print(function, end='')

    for index in range(len(i) - 1, 0 ,-1):
        if not i[index].isalpha():
            if i[index] == ']':
                print('[', end='')
            elif i[index] == '[':
                print(']', end='')
            else:
                print(i[index], end='')

    print(' ', end='')

    # 기본 변수명 출력
    for index in range(len(i)):
        if i[index].isalpha():
            print(i[index], end='')

    print(';')