# 연결 요소의 개수
# 연결 요소란 그래프로 이어진 것들
# 연결 요소의 개수란 그래프로 이어진 것들이 몇 개 존재하는지

# 1개로 다 이어질 경우 1개, 몇개 떨어져서 생성될 경우에는 몇개로 나옴
import sys
input = sys.stdin.readline
# 파이썬 특성상 재귀함수에 제한이 걸려있어 제한을 풀어줘야 한다.
sys.setrecursionlimit(10000)
n,m = map(int,input().split())
board = [[] for _ in range(n+1)]
dist = [False] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    # 서로 이어진 인덱스에 추가
    board[a].append(b)
    board[b].append(a)

# 입력한 인덱스가 방문하지 않았을경우 계속 돌림
def dfs(start):
    dist[start] = True
    for i in board[start]:
        if dist[i] == False:
            dfs(i)

cnt = 0
for i in range(1,n+1):
    if dist[i] == False:
        dfs(i)
        # DFS가 끝나면 그래프가 끝인 소리이니 1개 추가
        cnt += 1

print(cnt)