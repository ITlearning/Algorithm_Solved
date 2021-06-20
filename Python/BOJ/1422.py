# 숫자의 신
import sys
input = sys.stdin.readline
K,N = map(int,input().split())
board = [input().rstrip() for _ in range(K)]

board.sort(reverse=True)
tmp = N - K
t = 0
text = ""
for i in range(N):
    if tmp >= 0:
        text += board[t]
        tmp -= 1
    else:
        t += 1
        text += board[t]

print(text)