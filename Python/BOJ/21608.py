# 상어 초등학교
from collections import deque, Counter
from copy import deepcopy
N = int(input())

dx = [0,-1,0,1]
dy = [-1,0,1,0]

board = [[0 for _ in range(N)] for _ in range(N)]
number = [[] for _ in range((N*N)+1)]
peoples = []
picked = []

def check_near_friends(people):
    q = deque()
    for i in range(N):
        for j in range(N):
            if board[i][j] in number[people]:
                print(board[i][j], number[people])
                q.append([i,j])
    print(q)
    return q

def none_box_check(people):
    none_box = {}
    none_q = deque()
    while near:
        x,y = near.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0:
                    none_q.append([nx,ny])

    if len(none_q) == 1:
        return none_q[0] 
    elif len(none_q) == 0:
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    return [i,j]
    else:
        tmp_none = deepcopy(none_q)
    box = {}

    while none_q:
        x,y = none_q.popleft()
        for di in range(4):
            nx = x + dx[di]
            ny = y + dy[di]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0:
                    if (x,y) not in box:
                        box[x,y] = 1
                    else:
                        box[x,y] += 1

    if len(box) != 0:
        mx = max(box.values())
    else:
        return tmp_none[0]
    print("box",box)
    remake = []
    for i in box.items():
        if box[i[0]] == mx:
            remake.append(i)

    value = list(box.values())

    if len(remake) > 0:
        remake = sorted(remake, key=lambda x: (x[0][0],x[0][1]))
    print(remake)
    return remake[0][0]



def check_friends(x,y,index):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] in number[index]:
                cnt += 1
    
    if cnt == 0:
        return 0
    elif cnt == 1:
        return 1
    elif cnt == 2:
        return 10
    elif cnt == 3:
        return 100
    elif cnt == 4:
        return 1000


for _ in range(N*N):
    tmp = list(map(int,input().split()))
    index = tmp[0]
    numbers = tmp[1::]
    number[index] = numbers
    peoples.append(index)

for index, people in enumerate(peoples):
    if index == 0:
        board[1][1] = people
    else:
        # 주위 체크
        near = check_near_friends(people)
        # 인접 칸 체크
        location = none_box_check(people)
        board[location[0]][location[1]] = people

        for i in board:
            print(i)
        print()

answer = 0

for i in range(N):
    for j in range(N):
        num = check_friends(i,j,board[i][j])
        print(num)
        answer += num

print(answer)



    