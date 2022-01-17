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

controller = { "L": 1, "R": -1 }

for _ in range(t):
    board.append(list(input()))


for turtle in board:
    tmp_x = x()
    tmp_y = y()
    turtle_x = 0
    turtle_y = 0
    answer = 0
    for move in turtle:
        if move == "F":
            turtle_x += dx[axis]
            turtle_y += dy[axis]
        elif move == "B":
            turtle_x -= dx[axis]
            turtle_y -= dy[axis]
        else:
            axis += controller[move]
            if axis > 3:
                axis = 0
            elif axis < 0:
                axis = 3
        
        tmp_x.max_x = max(tmp_x.max_x, turtle_x)
        tmp_x.min_x = min(tmp_x.min_x, turtle_x)
        tmp_y.max_y = max(tmp_y.max_y, turtle_y)
        tmp_y.min_y = min(tmp_y.min_y, turtle_y)
    
    answer = (abs(tmp_x.max_x) + abs(tmp_x.min_x)) * (abs(tmp_y.max_y) + abs(tmp_y.min_y))

    print(answer)
    

