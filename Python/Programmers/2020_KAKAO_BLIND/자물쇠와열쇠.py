
def turn(key):
    n = len(key)
    m = len(key[0])
    tmp = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            tmp[j][n-i-1] = key[i][j]
    return tmp


def solution(key, lock):
    answer = True
    k = 0
    while k < 4:
        turn_key = turn(key)
        print(turn_key)

        #for i in range(len(turn_key[0])):
            

        key = turn_key[:]
        k+= 1

        

    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

solution(key, lock)