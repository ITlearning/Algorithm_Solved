# 컨베이어 벨트 위의 로봇
from collections import deque
N,K = map(int,input().split())
N = N*2 # N 값 2배
board = list(map(int,input().split())) # 벨트 내구성 입력
board = deque(board)
total = 0  # 단계 카운트와 동시에 로봇 카운터
robot = deque([0]*(N)) # 로봇 덱

while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    total += 1
    board.rotate(1) # deque에 rotate() 함수를 사용했다. 매개변수가 1일경우 시계방향 회전, 0일경우 반시계 방향
    robot.rotate(1) # 두개 다 한 칸 회전

    robot[(N//2)-1] = 0 # 내리는 위치의 로봇 내려주기 (문제에서 내리는 위치의 로봇은 내려주라고 하니)

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        # 1. 로봇이 이동하기 위해서 는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    tmp = [] # 로봇의 위치
    for i in range(N):
        if robot[i] > 0:
            tmp.append([robot[i],i]) # 로봇의 번호와 로봇의 인덱스 같이 저장
    tmp.sort() # 오름차순 정렬
    for (number, index) in tmp:
        if robot[index+1] == 0 and board[index+1] > 0: # 로봇이 있는 위치 바로 다음 인덱스의 이동 여부 체크
            robot[index] = 0 
            robot[index+1] = number
            board[index+1] -= 1 # 내구도 -1
    
    robot[(N//2)-1] = 0 # 내리는 위치의 로봇 내려주기 (여기서도 한 번 더 확인)

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if board[0] > 0:
        board[0] -= 1
        robot[0] = total + 1
    
    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않으면 1번으로 돌아간다.
    if board.count(0) >= K:
        break

print(total) # 답 출력

# Python3 : 시간 초과
# PyPy3 : 시간 3320m..