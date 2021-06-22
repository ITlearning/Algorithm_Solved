# 상하좌우 문제
# L = 왼쪽으로 한 칸 이동, R = 오른쪽으로 한 칸 이동
# U = 위로 한 칸 이동, D = 아래로 한 칸 이동

# 공간의 크기 N X N
N = int(input())
x = 1
y = 1
control = list(input().split())
con = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in control:
    nx = x + dx[con.index(i)]
    ny = y + dy[con.index(i)]
    if 1 <= nx < N and 1 <= ny < N:
        x,y = nx,ny
print(x,y)
