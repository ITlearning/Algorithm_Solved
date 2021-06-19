# 부분 합
import sys
input = sys.stdin.readline

N,S = map(int,input().split())

board = list(map(int,input().split()))

dist = [0] * (N+1)
for i in range(1,N+1):
    dist[i] = dist[i-1] + board[i-1]

answer = 9999999
start = 0
end = 1
while start != N:
    if dist[end] - dist[start] >= S:
        if end - start < answer:
            answer = end - start
        start += 1
    else:
        if end != N:
            end += 1
        else:
            start += 1

if answer != 9999999:
    print(answer)
else:
    print(0)