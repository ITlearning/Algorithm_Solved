# 소수
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

def prime_num(n):
    if n == 1 or n == 0:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
    return True

board = []
for i in range(n, m+1):
    if prime_num(i):
        board.append(i)

if len(board) == 0:
    print(-1)
else:
    print(sum(board))
    print(board[0])
