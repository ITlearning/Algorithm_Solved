# 반복수열
import sys
input = sys.stdin.readline

a,p = map(int, input().split())

d = 0
D = [a]
tmp = str(a)
while D.count(int(tmp)) < 2:
    total = 0
    if len(tmp) == 1:
        total += pow(int(tmp), p)
    elif len(tmp) == 2:
        total = pow(int(tmp[0]), p) + pow(int(tmp[1]), p)
    elif len(tmp) == 3:
        total = pow(int(tmp[0]), p) + pow(int(tmp[1]), p) + pow(int(tmp[2]), p)
    elif len(tmp) == 4:
        total = pow(int(tmp[0]), p) + pow(int(tmp[1]), p) + pow(int(tmp[2]), p) + pow(int(tmp[3]), p)
    elif len(tmp) == 5:
        total = pow(int(tmp[0]), p) + pow(int(tmp[1]), p) + pow(int(tmp[2]), p) + pow(int(tmp[3]), p) + pow(int(tmp[4]), p)
    elif len(tmp) == 6:
        total = pow(int(tmp[0]), p) + pow(int(tmp[1]), p) + pow(int(tmp[2]), p) + pow(int(tmp[3]), p) + pow(int(tmp[4]), p) + pow(int(tmp[5]), p)
    tmp = str(total)
    D.append(total)
print(D.index(int(tmp)))