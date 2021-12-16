# 캐슬 디펜스
from itertools import combinations
from heapq import heappop, heappush

n,m,d = map(int,input().split())
arrows_list = [i for i in range(m)]

arrows = tuple(combinations(arrows_list, 3))
insert = [list(map(int, input().rstrip().split())) for _ in range(n)]
board = []

# 적 세기 함수
def count_enemy():
    global board 
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 :
                cnt += 1
    
    return cnt

# 공격 함수
def attack(arrow_index):
    global board
    attack_list = []
    # 공격한 적인지 아닌지 체크용
    visited = [[False for _ in range(m)] for _ in range(n)]

    cnt = 0

    for arrow in arrows[arrow_index]:
        q = [] # [거리, x,y] 우선순위 큐에 삽입

        for i in range(n-1, -1, -1):
            for j in range(m):
                if board[i][j] == 1:
                    tmp = abs(n-i) + abs(arrow - j)
                    # 절댓값 비교해서 작으면 우선순위 큐에 넣기
                    if tmp <= d:
                        heappush(q, [tmp,j,i])
        
        # 우선순위 큐 안에 들어가 있으면
        if q:
            # 왼쪽이고 제일 가까운 위치의 좌표 뽑아내기
            distance,x,y = heappop(q)
            # 그리고 추가
            attack_list.append([y,x])

    # 추가한 위치에 적 제거
    for y,x in attack_list:
        if not visited[y][x]:
            visited[y][x] = True
            cnt += 1
            board[y][x] = 0

    return cnt

# 움직이기 함수
def move():
    global board
    # 제일 끝의 리스트 0으로 도배
    board[-1] = [0 for _ in range(m)]

    # 돌면서 하나씩 아래로 내리기
    for i in range(-1, -n, -1):
        board[i] = board[i-1]
    
    # 첫번째 리스트 0으로 초기화
    board[0] = [0 for _ in range(m)]


# 시작 함수
def start(arrow_index):
    cnt = 0
    
    # 적의 개수가 0이 될때까지 돌리기
    while count_enemy() != 0:
        cnt += attack(arrow_index)
        move()
    
    return cnt

answer = 0
# board로 복사 후 시작
for i in range(len(arrows)):
    board = [[insert[i][j] for j in range(m)] for i in range(n)]
    cnt = start(i)
    if answer < cnt:
        answer = cnt

print(answer)