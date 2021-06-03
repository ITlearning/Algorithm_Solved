# 경로 찾기
# 가중치 없는 방향 그래프 일때, 모든 정점에 대해서 a 에서 b로 가는 경로가 있는지
# 구하는 문제
import sys
input = sys.stdin.readline
n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int,input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            # 만일 [a][b] 가 1일 때 [a][k] 혹은 [k][b] 도 1일 경우 
            # 간선이 존재한다라는 뜻이니 1로 변경
            if board[a][b] == 1 or (board[a][k] == 1 and board[k][b] == 1):
                board[a][b] = 1

for a in range(n):
    for b in range(n):
        print(board[a][b], end=" ")
    print()