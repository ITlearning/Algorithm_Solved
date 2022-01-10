# 외계인의 기타연주
import sys
input = sys.stdin.readline
guitar = [[] for _ in range(7)]

n,m = map(int,input().split())
cnt = 0
for _ in range(n):
    jul, fret = map(int,input().split())

    if len(guitar[jul]) != 0:
        if guitar[jul][-1] > fret:
            while True:
                guitar[jul].pop()
                cnt += 1
                if len(guitar[jul]) == 0:
                    guitar[jul].append(fret)
                    cnt += 1
                if guitar[jul][-1] < fret:
                    guitar[jul].append(fret)
                    cnt += 1
                    break
                elif guitar[jul][-1] == fret:
                    break
        
        elif guitar[jul][-1] == fret:
            continue
        else:
            guitar[jul].append(fret)
            cnt += 1
    else:
        guitar[jul].append(fret)
        cnt += 1


print(cnt)