# 스티커 붙이기

def rotate(key):
    #key = [k[::-1] for k in zip(*key)]
    return list(zip(*key[::-1]))


def check_paste(i,j,key):
    kr, kc = len(key), len(key[0])
    for ki in range(kr):
        for kj in range(kc):
            if board[i+ki][j+kj] == 1 and key[ki][kj] == 1:
                return False

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
        for i in range(n - (r-1)):
            for j in range(m - (c-1)):
                if check_paste(i,j, key):
                    flag = True
                    break
            if flag:
                break

        if not flag:
            if turn == 0:
                break
            key = rotate(key)
            turn = (turn + 1) % 4
        else:
            break

answer = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            answer += 1

print(answer)