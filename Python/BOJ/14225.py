# 부분수열의 합
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())

board = list(map(int,input().split()))

total = board

def count(index, sum):
    if index == n:
        return 0
    total.append(sum+board[index])
    count(index+1, sum+board[index])
    count(index+1, sum)

count(0,0)
t = set(total)

answer = 0
for i in range(max(t)):
    if i+1 not in t:
        answer = i + 1
        break

print(answer if answer else max(t)+1)
