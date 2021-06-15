# RGB 거리

# 위 문제의 점화식을 구하는게 제일 중요하다.
# DP문제이기 때문 ㅎ

# 문제에서 제한 조건을 1번집의 색은 2번 집의 색과 같지 않아야 한다.
# N 번집의 색은 N-1번 집의 색과 같지 않아야 한다.
# 그러니까 각 집은 이전 집과 색이 달라야 하고, 양 끝이 아닌 집은 이전 집과 다음 집과의 색이 달라야 한다.
# 라고 정의한다. 따라서 이걸 간단하게 생각하면, 이전 집과의 색이 달라야 한다.
# 우리는 어떤 집을 칠할 때 그 집에 쓸 수 있는 색깔은 바로 앞집에서 쓴 색이 아니면 다 가능하다는 것이다.

# 그리고 문제에서 나오는 수들은 모두 비용이기 때문에, 집을 칠하면서 비용은 당연히 자연스레 늘어나는 것이다.
# 최소바용을 구하는 문제이니 min을 사용하면 된다.
# 그래서 점화식을 생각해보면,
#  R = D[R] + min(D[n-1][B], D[n-1][G]) 
#  G = D[n][G] + min(D[n-1][B], D[n-1][R])
#  B = D[n][B] + min(D[n-1][G], D[n-1][R])
# 이렇게 될듯 하다.

import sys
input = sys.stdin.readline
t = int(input())
board = []

for _ in range(t):
    board.append(list(map(int,input().split())))

for i in range(1,len(board)):
    board[i][0] = board[i][0] + min(board[i-1][1], board[i-1][2])
    board[i][1] = board[i][1] + min(board[i-1][0], board[i-1][2])
    board[i][2] = board[i][2] + min(board[i-1][0], board[i-1][1])

print(min(board[t-1][0], board[t-1][1], board[t-1][2]))