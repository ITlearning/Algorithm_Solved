# ATM
import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int, input().split()))
board.sort()
tmp = 0
result = []
for i in board:
    tmp += i
    result.append(tmp)
answer = 0
for i in result:
    answer += i
print(answer)