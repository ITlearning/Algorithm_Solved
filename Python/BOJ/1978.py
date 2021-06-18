# 소수 찾기
import math
import sys
input = sys.stdin.readline
def prime_num(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True

n = int(input())
board = list(map(int,input().split()))
answer = []
for i in board:
    num = int(i)
    if prime_num(num):
        answer.append(num)

print(len(answer))