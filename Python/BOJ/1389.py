from sys import stdin
from math import inf
n,m = map(int,stdin.readline().split())
s = [[0]* n for i in range(n)]

for i in range(m):
    a,b = map(int, stdin.readline().split())
    s[a-1][b-1] = 1
    s[b-1][a-1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                continue
            elif s[i][k] and s[k][j]:
                if s[i][j] == 0:
                    s[i][j] = s[i][k] + s[k][i]
                else:
                    s[i][j] = min(s[i][j],s[i][k] + s[k][j])
result = inf
for i in range(n) :
    sum = 0
    for j in range(n) :
        sum += s[i][j]
    if result > sum:
        result = sum
        p = i
print(p+1)

# https://pacific-ocean.tistory.com/278

# https://donghak-dev.tistory.com/10