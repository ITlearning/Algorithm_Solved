# 거북이
from copy import deepcopy
t = int(input())
board = []

# 상, 우, 하, 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

axis = 0
turtle_x = 0
turtle_y = 0

# x,y 값 저장할 클래스
class x:
    max_x = 0
    min_x = 0

    def __init__(self) -> None:
        pass

class y:
    max_y = 0
    min_y = 0

    def __init__(self) -> None:
        pass


# L,R 작업 처리할 딕셔너리
controller = { "L": 1, "R": -1 }


# 1. 입력
for _ in range(t):
    board.append(list(input()))

# 2. board 입력 리스트 돌면서 작업 시작
for turtle in board:
    # 값 초기화
    tmp_x = x()
    tmp_y = y()
    turtle_x = 0
    turtle_y = 0
    answer = 0

    for move in turtle:
        # F일 경우 +
        if move == "F":
            turtle_x += dx[axis]
            turtle_y += dy[axis]
        # B일 경우 -
        elif move == "B":
            turtle_x -= dx[axis]
            turtle_y -= dy[axis]
        else:
            # 나머지 입력이면 위치 변경
            axis += controller[move]
            if axis > 3:
                axis = 0
            elif axis < 0:
                axis = 3
        
        # max 값에는 제일 큰 좌표 입력, min값에는 제일 작은 좌표 입력
        tmp_x.max_x = max(tmp_x.max_x, turtle_x)
        tmp_x.min_x = min(tmp_x.min_x, turtle_x)
        tmp_y.max_y = max(tmp_y.max_y, turtle_y)
        tmp_y.min_y = min(tmp_y.min_y, turtle_y)
    
    # answer에 현재 저장된 max,min 절댓값 곱하기
    answer = (abs(tmp_x.max_x) + abs(tmp_x.min_x)) * (abs(tmp_y.max_y) + abs(tmp_y.min_y))

    print(answer)
    

