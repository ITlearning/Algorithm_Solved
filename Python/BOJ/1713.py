# 후보 추천하기
import sys
from collections import deque
#input = sys.stdin.readline

n = int(input())
m = int(input())
cnt = 0
dic = {}

numbers = list(map(int,input().split()))

for number in numbers:
    if cnt >= n and number not in dic:
        del dic[min(dic, key=lambda x: dic[x])]
    if number in dic:
        dic[number][0] += 1
    else:
        dic[number] = [1,cnt]
        cnt += 1

answer = sorted(dic.items())
for index, item in enumerate(answer):
    if index == len(answer)-1:
        print(item[0], end="")
    else:
        print(item[0], end=" ")