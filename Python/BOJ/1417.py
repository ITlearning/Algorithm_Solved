# 국화의원 선거

n = int(input())
d = []
for i in range(n) :
    x = int(input())
    d.append(x)
dasom = d[0]
other = d[1:len(d)]

if n == 1:
    print(0)
else:
    count = 0
    other = sorted(other,reverse=True)
    while other[0] >= dasom :
        dasom += 1
        other[0] -= 1
        count += 1
        other = sorted(other, reverse=True)
    print(count)

