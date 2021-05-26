# 상하좌우 문제

n = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
    #  L R U D
con = ['L', 'R', 'U', 'D']

move = list(input().split())
x = 0
y = 0
for i in move:
    if i in con:
        for j in range(len(con)):
            if i == con[j]:
                xn = x + dx[j]
                yn = y + dy[j]
                if xn < 0 or xn >= n or yn < 0 or yn >= n: continue 
                x = xn
                y = yn


print(x+1,y+1)