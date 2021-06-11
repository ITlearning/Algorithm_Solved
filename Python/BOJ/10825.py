# 국영수
# 처음에는 무식하게 그냥 if 문으로 나눠서 했더니 시간초과가 나왔다.
# 파이썬에는 람다로 다 처리가 가능하다;
import sys
input = sys.stdin.readline
t = int(input())
board = []

for _ in range(t):
    name, korean, english, math = input().split()
    board.append([name, korean, english, math])

board.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in board:
    print(i[0])