# 톱니바퀴
from collections import deque

gear = []
for _ in range(4):
    tmp = map(int,input())
    gear.append(list(tmp))
k = int(input())


def rotate(x, dir):
    if dir == 1:
        gear[x].insert(0, gear[x].pop())
    elif dir == -1:
        gear[x].append(gear[x].pop(0))

for i in range(k):
    number, direction = map(int,input().split())
    dist = [[number-1, direction]]
    z = direction
    x = number -1
    while x+1 <= 3:
        if gear[x][2] != gear[x+1][6]:
            z = -z
            dist.append([x+1, z])
        else:
            break
        x += 1
    
    x = number-1
    z = direction
    while x -1 >= 0:
        if gear[x][6] != gear[x-1][2]:
            z = -z
            dist.append([x-1, z])
        else:
            break
        x -= 1
    
    for x, dir in dist:
        rotate(x,dir)

result = (gear[0][0] * 1) + (gear[1][0] * 2) + (gear[2][0] * 4) + (gear[3][0] * 8)
print(result)