# 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

poketmon = []
for i in range(1,n+1):
    name = input().rstrip()
    poketmon.append(name)

for i in range(m):
    index = input().rstrip()
    if 48 <= ord(index[0]) <= 57:
        print(poketmon[int(index)-1])
    else:
        tmp = poketmon.index(index)
        print(tmp + 1)
