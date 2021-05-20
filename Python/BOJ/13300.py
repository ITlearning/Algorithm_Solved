B = [0 for i in range(6)]
G = [0 for i in range(6)]
a,b = input().split()
a = int(a)
b = int(b)
for i in range(a) :
    c,d = input().split()
    c = int(c)
    d = int(d)
    if c == 0 :
        if d != 0 :
            G[d-1] += 1
    elif c == 1:
        if d != 0 :
            B[d-1] += 1
cnt = 0  
for i in range(6) :
    girl = G[i] // b
    boy = B[i] // b
    if G[i] % b != 0 :
        girl += 1
    if B[i] % b != 0 :
        boy += 1
    cnt += girl + boy

print(cnt)