# 녹색 옷 입은 애가 젤다지?
import heapq
from copy import deepcopy

dx = [0,-1,0,1]
dy = [-1,0,1,0]

cnt = 1

# 0 나올 때 까지 계속 돌리기
while True:
    n = int(input())
    board = []

    if n == 0:
        break

    # 입력받기
    for _ in range(n):
        board.append(list(map(int,input().split())))

    # 방문여부 + 최소 루피 측정 리스트
    visited = [[99999 for _ in range(n)] for _ in range(n)]

    q = []
    # 왼쪽 제일위의 수를 우선순위 큐의 가장 먼저 넣어주기
    heapq.heappush(q, (board[0][0], (0,0)))
    # 방문 표시로 첫 번째 위치 숫자 넣기
    visited[0][0] = deepcopy(board[0][0])

    # 다익스트라 돌리기
    while q:
        num, (x,y) = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 돌면서 크기에 어긋나지 않을 경우
            if 0 <= nx < n and 0 <= ny < n:
                # 방문을 하지 않았을 경우
                if visited[nx][ny] == 99999:
                    # 방문 표시
                    visited[nx][ny] = board[nx][ny] + num
                    # 그리고 우선순위 큐에 저장
                    heapq.heappush(q, (visited[nx][ny], [nx,ny]))
                # 방문을 했지만, 더 적은 루피로 이동할 수 있을 경우
                elif visited[nx][ny] > board[nx][ny] + num:
                    # 그 값으로 갱신
                    visited[nx][ny] = board[nx][ny] + num
                    # 우선순위 큐에 저장
                    heapq.heappush(q, (visited[nx][ny], [nx,ny]))
                
                # 방문도 했고, 저장되어 있는 루피의 수가 더 적을 경우
                else:
                    # 건너뛰기
                    continue
    # 답 출력
    print("Problem "+str(cnt)+":", visited[n-1][n-1])
    cnt += 1
