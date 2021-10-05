# 이동하기
# 준규는 N×M 크기의 미로에 갇혀있다. 미로는 1×1크기의 방으로 나누어져 있고, 각 방에는 사탕이 놓여져 있다. 
# 미로의 가장 왼쪽 윗 방은 (1, 1)이고, 가장 오른쪽 아랫 방은 (N, M)이다.

# 준규는 현재 (1, 1)에 있고, (N, M)으로 이동하려고 한다. 
# 준규가 (r, c)에 있으면, (r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있고, 각 방을 방문할 때마다 방에 놓여져있는 사탕을 모두 가져갈 수 있다. 
# 또, 미로 밖으로 나갈 수는 없다.

# 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하시오.


import sys
input = sys.stdin.readline
n,m = map(int,input().split())
# 1. 미로 크기 만큼 d 생성
d = [[0 for _ in range(m+1)] for _ in range(n+1)]

board = []
# 2. 미로 입력받기
for i in range(n):
    board.append(list(map(int,input().split())))

# 3. 문제에서 얘기한대로 아래, 오른쪽, 대각선 오른쪽의 값을 저장하려는 인덱스 기준으로 처리
for i in range(1,n+1):
    for j in range(1,m+1):
        # 확인을 하면서 가장 큰 수를 더하기
        d[i][j] = board[i-1][j-1] + max(d[i-1][j], d[i][j-1], d[i-1][j-1])

# 4. 답 출력
print(d[n][m])