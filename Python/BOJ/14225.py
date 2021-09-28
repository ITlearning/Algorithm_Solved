# 부분수열의 합
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())

board = list(map(int,input().split()))

total = board
# 찾아본 풀이
def count(index, sum):
    if index == n:
        return 0
    total.append(sum+board[index])
    # 재귀적으로 모든 경우 확인
    count(index+1, sum+board[index])
    count(index+1, sum)

count(0,0)
# 중복 제거
t = set(total)

answer = 0
# for문 돌면서 다음 수가 없으면 답으로 선택
for i in range(max(t)):
    if i+1 not in t:
        answer = i + 1
        break

# 그게 아니고 그냥 for문 돌아버렸으면 max+1 값이 답
print(answer if answer else max(t)+1)
