# 연구소
import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
graph_copy = copy.deepcopy(graph)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

safe_region = 0 # 최대 안전 영역


def dfs(x,y,sel_wall):
    sel_wall[x][y] = 2 # 바이러스로 변경

    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if sel_wall[nx][ny] == 0: # 바이러스 퍼뜨리기
                dfs(nx,ny, sel_wall)


# 벽 선택하기
def select_wall(start, count):
    global safe_region

    if count == 3: # 벽이 3개 선택된 경우 실행
        sel_wall = copy.deepcopy(graph_copy) # 벽이 선택된 그래프

        for i in range(N):
            for j in range(M):
                if sel_wall[i][j] == 2:
                    dfs(i,j,sel_wall)
        safe_count = sum(_.count(0) for _ in sel_wall) # 안전 영역 개수 계산
        safe_region = max(safe_region, safe_count) # 최대 안전 영역 개수 갱신
        return
    else: # 벽이 3개 선택되지 않은 경우
        for i in range(start, N*M): # 브루트-포스로 벽 선택
            r = i // M # M으로 나눈 몫은 행
            c = i % M # M으로 나눈 나머지는 열
            if graph_copy[r][c] == 0: # 해당구역이 0인 경우에
                graph_copy[r][c] = 1 # 벽으로 선택
                select_wall(i, count+1) # 다음 벽 선택
                graph_copy[r][c] = 0 # 되돌리기

select_wall(0,0)
print(safe_region)