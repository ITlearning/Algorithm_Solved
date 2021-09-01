def turn(key):
    return list(zip(*key[::-1]))
    '''
    n = len(key)
    m = len(key[0])
    tmp = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            tmp[j][n-i-1] = key[i][j]
    return tmp
    '''


def insert(x,y,turn_key, double_lock, M):
    for i in range(M):
        for j in range(M):
            #print(double_lock)
            double_lock[x+i][y+j] += turn_key[i][j]

def reload(x,y,turn_key, double_lock, M):
    for i in range(M):
        for j in range(M):
            #print(double_lock)
            double_lock[x+i][y+j] -= turn_key[i][j]

def check(N,M, double_lock):
    for i in range(N):
        for j in range(N):
            if double_lock[M+i][M+j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    double_lock = [[0] * (m*2+n) for _ in range(m*2+n)] 

    for i in range(n):
        for j in range(n):
            double_lock[m+i][m+j] = lock[i][j]

    
    turn_key = key
    for _ in range(4):
        turn_key = turn(turn_key)
        for i in range(1, n+m):
            for j in range(1, n+m):
                insert(i,j,turn_key,double_lock, m)
                if (check(n,m,double_lock)):
                    return True
                reload(i,j,turn_key,double_lock, m)

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))

# 2시간 35분 56초