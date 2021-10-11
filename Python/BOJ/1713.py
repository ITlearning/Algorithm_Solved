# 후보 추천하기
import sys
from collections import deque
#input = sys.stdin.readline

n = int(input())
m = int(input())
cnt = 0
board = [0 for _ in range(101)]
stack = []

numbers = list(map(int,input().split()))
#print(numbers)
for number in numbers:
    if cnt < n:
        if number not in stack:
            stack.insert(0,number)
            board[number] += 1
            cnt += 1
        else:
            board[number] += 1
    else:
        if number not in stack: 
            
        else:
            board[number] += 1

answer = stack

answer.sort()

for i in answer:
    print(i, end=" ")