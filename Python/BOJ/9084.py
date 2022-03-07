# 동전
import sys
read = sys.stdin.readline
 
T = int(read())
 
while T:
    N = int(read())
    coin = list(map(int, read().split()))
    M = int(read())
    d = [0 for _ in range(M+1)]
    d[0] = 1
 
    for i in range(N):
        for j in range(coin[i], M+1):
            d[j] += d[j-coin[i]]
 
    print(d[M])
    T -= 1
