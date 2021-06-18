# N번쨰 큰 수
import sys
input = sys.stdin.readline
t = int(input())
while t != 0:
    board = list(map(int,input().split()))
    board.sort(reverse=True)
    print(board[2])
    t -= 1