# 스티커 붙이기

# 90도 시계방향 회전 함수
def rotate(key):
    return list(zip(*key[::-1]))

# 체크하고 붙이는 함수
def check_paste(i,j,key):
    kr, kc = len(key), len(key[0])
    for ki in range(kr):
        for kj in range(kc):
            # 노트북 리스트와 키(스티커)를 비교하면서 중복되면 False
            if board[i+ki][j+kj] == 1 and key[ki][kj] == 1:
                return False
    
    # 그게 아니고 잘 넘겨왔으면 붙이기 시작
    for ci in range(kr):
        for cj in range(kc):
            if key[ci][cj] == 1:
                board[i+ci][j+cj] = 1

    return True

n,m,k = map(int,input().split())

board = [[0 for _ in range(m)] for _ in range(n)]


for _ in range(k):
    r,c = map(int,input().split())
    key = []

    for i in range(r):
        key.append(list(map(int,input().split())))

    turn = 1
    while True:
        flag = False
        r,c = len(key), len(key[0])
        # 키 크기만큼 가야 나머지 부분까지 탐색 가능하기 때문에 이렇게 함
        # 그 이상으로 가면 인덱스 초과
        for i in range(n - (r-1)):
            for j in range(m - (c-1)):
                # 체크해서 True가 나오면 붙인거니 종료
                if check_paste(i,j, key):
                    flag = True
                    break
            # flag도 같이 바뀌었으니 종료
            if flag:
                break
        
        # 근데 못붙였으면 여기로
        if not flag:
            # 4방향 다 돌았으면 종료
            if turn == 0:
                break
            # 방향 돌리고 다시 위로
            key = rotate(key)
            turn = (turn + 1) % 4
        else:
            break

answer = 0

# 다 붙이고 스티커 크기 세기
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            answer += 1

print(answer)