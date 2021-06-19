# 단지번호 붙이기
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
board = []
dan = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for i in range(N):
    num = list(input().rstrip())
    board.append(list(num))
cnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == '0': continue
        cnt += 1
        num = 0
        board[i][j] = '0'
        q = deque()
        q.append((i,j))
        while q:
            num += 1
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                if board[nx][ny] == '0' : continue
                board[nx][ny] = '0'
                q.append((nx,ny))
        dan.append(num)

print(len(dan))
dan.sort()
for i in dan:
    print(i)