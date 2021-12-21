# 녹색 옷 입은 애가 젤다지?
import heapq
from copy import deepcopy

dx = [0,-1,0,1]
dy = [-1,0,1,0]

cnt = 1

while True:
    n = int(input())
    board = []

    if n == 0:
        break

    for _ in range(n):
        board.append(list(map(int,input().split())))

    visited = [[99999 for _ in range(n)] for _ in range(n)]

    q = []
    # 왼쪽 제일위의 수를 가장 먼저 넣어주기
    heapq.heappush(q, (board[0][0], (0,0)))
    visited[0][0] = deepcopy(board[0][0])

    while q:
        num, (x,y) = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 99999:
                    visited[nx][ny] = board[nx][ny] + num
                    heapq.heappush(q, (visited[nx][ny], [nx,ny]))
                elif visited[nx][ny] > board[nx][ny] + num:
                    visited[nx][ny] = board[nx][ny] + num
                    heapq.heappush(q, (visited[nx][ny], [nx,ny]))
                else:
                    continue
    
    print("Problem "+str(cnt)+":", visited[n-1][n-1])
    cnt += 1