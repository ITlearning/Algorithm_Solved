# K번째 수
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
#board = [i*j for i in range(1,n+1) for j in range(1, n+1)]

print(k//n)