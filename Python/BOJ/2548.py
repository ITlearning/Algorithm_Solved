# 대표 자연수
import sys
import heapq
input = sys.stdin.readline

n = int(input())

board = list(map(int,input().split()))

total = [] # 선택된 숫자의 차이 합을 넣어놓을 리스트
for i in range(n):
    tmp = 0
    for j in board: # 각 숫자를 돌면서 차이를 tmp에 저장
        tmp += abs(board[i] - j)
    heapq.heappush(total, [tmp,board[i]]) # 그리고 선택된 숫자와 차이의 합 tmp를 같이 넣어줌(최소 힙 이용)

print(total[0][1]) # 제일 앞의 수 출력

# PyPy 통과