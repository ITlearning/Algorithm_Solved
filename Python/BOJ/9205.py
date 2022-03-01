# 맥주 마시면서 걸어가기
from collections import deque
import sys

input = sys.stdin.readline

# 테스트 케이스 입력
t = int(input())

def bfs(x,y):
    q,c = deque(), []
    q.append([x,y, 20])
    c.append([x,y, 20])
    while q:
        x, y, beer = q.popleft()
        # 목적지에 도달하면 종료
        if x == x1 and y == y1:
            print("happy")
            return
        # board에 저장된 nx,ny 값 돌려보기
        for nx,ny in board:
            # 만일 지금 이 값이 c 안에 없으면
            if [nx,ny,20] not in c:
                # 현재 뽑은 거리와 for문 돌린 거리의 맨해튼 거리를 구하고 난 뒤
                l1 = abs(nx - x) + abs(ny - y)
                # beer의 값이 l1의 값보다 클 경우에
                if beer * 50 >= l1:
                    # 그 값을 q와 c에 넣어주기 
                    q.append([nx,ny,20])
                    c.append([nx,ny,20])
    # 답을 찾지 못했을 경우 sad 출력
    print("sad")
    return


while t:
    # 맥주 파는 편의점 개수
    n = int(input())
    # 상근이 집
    input_x, input_y = map(int,input().split())
    board = []
    # 편의점 좌표 입력
    for _ in range(n):
        x,y = map(int,input().split())
        board.append([x,y])
    
    # 락 페스티벌 좌표
    x1,y1 = map(int,input().split())

    # board에 입력
    board.append([x1,y1])

    # bfs 시작
    bfs(0,0)
    t -= 1
