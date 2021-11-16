# 경쟁적 전염
from collections import deque
n,m = map(int,input().split())

board = []
sort_list = []
sort = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 먼저 입력받은 숫자들에 대한 인덱스 뽑아내기
for i in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    for index, num in enumerate(tmp):
        if num > 0:
            sort_list.append([i,index,num])

# [x,y,num] 으로 구성된 리스트 입력받은 숫자 기준으로 정렬
sort_list.sort(key=lambda x : x[2])

# 덱에 옮김
q = deque(sort_list)
s,answer_x,answer_y = map(int,input().split())

time = 0  # 진행된 시간 기록 변수
while time < s:
    time += 1
    cnt = len(q)  # 이번 턴에 돌려야할 바이러스 개수
    while cnt > 0:  # 바이러스 개수가 다 끝날 때 까지 돌림 (한턴 종료 하기 위해서)
        x,y, pop_num = q.popleft()
        for cur in range(4):
            nx = x + dx[cur]
            ny = y + dy[cur]
            if 0 <= nx < n and 0 <= ny < n:
                # 0이면 아직 방문 안한거니까 전염 시킴
                if board[nx][ny] == 0:
                    board[nx][ny] = pop_num
                    q.append([nx,ny, pop_num])
        cnt -= 1  # 전염 시켰으면 하나 빼기

print(board[answer_x - 1][answer_y - 1])