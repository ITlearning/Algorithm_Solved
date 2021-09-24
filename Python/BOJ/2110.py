# 공유기 설치
import sys
from itertools import combinations
input = sys.stdin.readline

n,c = map(int,input().split())

board = []

for _ in range(n):
    num = int(input())
    board.append(num)
board.sort()

def binary_search(start,end):
    while start <= end:

        mid = (start + end) // 2
        select = board[0]
        count = 1
        for i in range(1,len(board)):
            if board[i] >= mid + select:
                count += 1
                select = board[i]

        if count >= c:
            global answer
            answer = mid
            start = mid + 1
        else:
            end = mid - 1


answer = 0
start = 1
end = board[-1] - board[0]
binary_search(start,end)

print(answer)