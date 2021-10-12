# 후보 추천하기
import sys
from collections import deque
#input = sys.stdin.readline

n = int(input())
m = int(input())
cnt = 0
dic = {}

numbers = list(map(int,input().split()))
# 입력받은 번호 돌리기
for number in numbers:
    # 사진틀의 개수가 넘어갔고 딕셔너리 내에 이름이 존재하지 않을 경우
    if cnt >= n and number not in dic:
        # 추천수가 제일 적은 수를 삭제(단, 이렇게 할 경우 추천수가 같으면 가장 오래된 수도 나옴)
        del dic[min(dic, key=lambda x: dic[x])]
    # 그게 아니고 디셔너리 내에 이름이 있으면
    if number in dic:
        # 단순 카운트
        dic[number][0] += 1
    else:
        # 없으면 딕셔너리 생성
        # 앞의 수는 횟수를 의미, 뒤 cnt는 순서
        dic[number] = [1,cnt]
        cnt += 1

answer = sorted(dic.items())
for index, item in enumerate(answer):
    if index == len(answer)-1:
        print(item[0], end="")
    else:
        print(item[0], end=" ")