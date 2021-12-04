# 배열 돌리기 3
from copy import deepcopy

# 1. 상하반전
def rotate_one(box):
    # 아래쪽부터 다 땡겨와서 리스트로 표현
    ret = list(box[::-1])
    return ret

# 2. 좌우반전
def rotate_two(box):
    ret = list(zip(*box[::-1])) # 시계방향 90도 회전
    an = list(ret[::-1])        # 회전한 box에서 반대로 정렬
    original = list(map(list, zip(*an)))[::-1] # 그거 다시 반시계방향으로 돌리기

    return original

# 3. 오른쪽 90도
def rotate_three(box):
    ret = list(zip(*box[::-1])) # 시계방향 90도 회전
    return ret

# 4. 왼쪽 90도
def rotate_four(box):
    ret = list(map(list, zip(*box)))[::-1]
    return ret

# 5,6. 등분해서 위치 바꾸기
def rotate_slice(box, index):
    # board 를 4등분
    box_one = []
    box_two = []
    box_three = []
    box_four = []

    # 나중에 합쳐서 보낼 리스트
    ret = [[0 for _ in range(M)] for _ in range(N)]

    # 1번 등록
    for i in range(N//2):
        tmp = []
        for j in range(M//2):
            tmp.append(box[i][j])
        box_one.append(tmp)
    
    # 2번 등록
    for i in range(N//2):
        tmp = []
        for j in range(M//2, M):
            tmp.append(box[i][j])
        box_two.append(tmp)

    # 3번 등록
    for i in range(N//2, N):
        tmp = []
        for j in range(M//2, M):
            tmp.append(box[i][j])
        box_three.append(tmp)
    
    # 4번 등록
    for i in range(N//2, N):
        tmp = []
        for j in range(M//2):
            tmp.append(box[i][j])
        box_four.append(tmp)

    # 입력에서 5를 입력받았을 때
    if index == 5:
        for i in range(N):
            for j in range(M):
                # 1번 위치 = 4번 박스가 위치해야 하는 곳
                if i < N//2 and j < M//2:
                    ret[i][j] = box_four[i][j]
                # 2번위치 = 1번 박스가 위치해야 하는 곳
                elif i < N//2 and j >= M//2:
                    ret[i][j] = box_one[i][j - M//2]
                # 3번위치 = 2번 박스가 위치해야 하는 곳
                elif i >= N//2 and j >= M//2:
                    ret[i][j] = box_two[i - N//2][j - M//2]
                # 4번위치 = 3번 박스가 위치해야 하는 곳
                elif i >= N//2 and j < M//2:
                    ret[i][j] = box_three[i - N//2][j]
    
    # 입력에서 6을 입력받았을 때
    elif index == 6:
        for i in range(N):
            for j in range(M):
                # 1번 위치 = 2번 박스가 위치해야 하는 곳
                if i < N//2 and j < M//2:
                    ret[i][j] = box_two[i][j]
                # 2번위치 = 3번 박스가 위치해야 하는 곳
                elif i < N//2 and j >= M//2:
                    ret[i][j] = box_three[i][j - M//2]
                # 3번위치 = 4번 박스가 위치해야 하는 곳
                elif i >= N//2 and j >= M//2:
                    ret[i][j] = box_four[i - N//2][j - M//2]
                # 4번위치 = 3번 박스가 위치해야 하는 곳
                elif i >= N//2 and j < M//2:
                    ret[i][j] = box_one[i - N//2][j]

    # 바뀐 리스트 리턴
    return ret


N,M,R = map(int,input().split())
board = []

for _ in range(N):
    board.append(list(map(int,input().split())))

rotate_list = list(map(int,input().split()))

# 입력받은 회전 적용
for rotate in rotate_list:
    if rotate == 1:
        tmp = rotate_one(board)
        board = deepcopy(tmp)
    elif rotate == 2:
        tmp = rotate_two(board)
        board = deepcopy(tmp)
    elif rotate == 3:
        tmp = rotate_three(board)
        board = deepcopy(tmp)
    elif rotate == 4:
        tmp = rotate_four(board)
        board = deepcopy(tmp)
    elif rotate == 5:
        tmp = rotate_slice(board, rotate)
        board = deepcopy(tmp)
    elif rotate == 6:
        tmp = rotate_slice(board, rotate)
        board = deepcopy(tmp)

    # 회전이 끝나고 난 뒤의 board의 N,M을 업데이트 시켜줘야 함
    # 이거 안해주면 index 에러 남
    N = len(board)
    M = len(board[0])

# 출력  
for i in board:
    print(*i)