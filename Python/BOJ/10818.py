# 최소, 최대
import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int,input().split()))

board.sort()

print(board[0], board[len(board)-1])