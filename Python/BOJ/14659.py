# 한조서열정리하고옴ㅋㅋ
import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int,input().split()))
tmp = 0
cnt = 0
result = 0
for i in board:
    tmp = max(tmp, i)
    if tmp == i :
        cnt = 0
    elif tmp > i:
        cnt += 1
    result = max(result,cnt)


print(result)