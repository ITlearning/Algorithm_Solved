# 약수 구하기
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
board = []
for i in range(1, N+1):
    if N % i == 0 :
        board.append(i)
board.sort()
if len(board) < K:
    print(0)
else:
    print(board[K-1])