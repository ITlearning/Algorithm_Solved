# 배열 돌리기 1

n,m,r = map(int,input().split())

board = []

def rotate(start):
    # 각 모서리에 위치한 숫자들 뽑아내기
    left_top = board[start][start]
    right_top = board[start][m-start-1]
    left_bottom = board[n-start-1][start]
    right_bottom = board[n-start-1][m-start-1]

    #print(left_top, right_top, left_bottom, right_bottom)
    # 위쪽
    for i in range(start+1, m-start):
        board[start][i-1] = board[start][i]
    # 왼쪽
    for i in range(n-start-1, start,-1):
        board[i][start] = board[i-1][start]
    # 아래쪽
    for i in range(m-start-1, start+1, -1):
        board[n-start-1][i] = board[n-start-1][i-1]
    # 오른쪽
    for i in range(start+1, n-start):
        board[i-1][m-start-1] = board[i][m-start-1]
    
    # 뽑아낸 숫자 옮겨진 곳에 다시 넣기
    board[start+1][start] = left_top
    board[start][m-start-2] = right_top
    board[n-start-1][start+1] = left_bottom
    board[n-start-2][m-start-1] = right_bottom

for _ in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)

number = min(n,m)

# 입력 받은 r 만큼 횟수 돌리고
for _ in range(r):
    # 각 행렬중 작은 수 기준으로 2로 나누고 rotate() 함수 실행
    for k in range(number//2):
        rotate(k)

# * 을 쓰면 리스트가 제거되고 안에 원소들만 나옴
# 이번에 처음 알게됨
for bo in board:
    print(*bo)