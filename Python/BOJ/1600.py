# 말이 되고픈 원숭이 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
import sys
from collections import deque
input = sys.stdin.readline

# 말 처럼 움직이는 모션 ㅋㅋㅋㅋㅋ
e_dx = [-2,-1,1,2,2,1,-1,-2]
e_dy = [-1,-2,-2,-1,1,2,2,1]

# 그냥 상하좌우 이동
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 말처럼 움작알 수 있는 횟수
k = int(input())
W,H = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(H)]
# 방문 카운트 해주는 리스트를 3차원 리스트로 생성하여, 각 횟수에 따라서 카운트를 세준다.
# 그리고 마지막으로 카운트 된 수를 리턴
# 흠..더 공부가 필요하다.
dist = [[[0 for _ in range(31)] for _ in range(W)] for _ in range(H)]

q = deque()
q.append((0,0,k))
answer = -1
def dfs():
    while q:
        x,y,z = q.popleft()

        if x == H-1 and y == W-1: 
            return dist[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != 1 and dist[nx][ny][z] == 0:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx,ny,z))

        if z > 0:
            for i in range(8):
                nx = x + e_dx[i]
                ny = y + e_dy[i]
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != 1 and dist[nx][ny][z-1] == 0:
                    dist[nx][ny][z-1] = dist[x][y][z] + 1
                    q.append((nx,ny,z-1))
    return -1

print(dfs())

# https://pacific-ocean.tistory.com/393