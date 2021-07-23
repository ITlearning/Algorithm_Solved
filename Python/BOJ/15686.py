# 치킨 배달
N,M = map(int,input().split())

board = []
people = []
shop = []
for i in range(N):
    board.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            people.append([i+1,j+1])
        elif board[i][j] == 2:
            shop.append([i+1,j+1, 0])
total = []

for p in range(len(people)):
    tmp = 1e9
    big_index = 0
    for s in range(len(shop)):
        big = abs(people[p][0] - shop[s][0]) + abs(people[p][1] - shop[s][1])
        if tmp >= big:
            tmp = big
            big_index = s
    shop[big_index][2] += 1


# 정렬에서 계속 문제 생긴다. 이거 어떻게 고칠까 고민좀 해야겠는걸?

shop.sort(reverse=True,key=lambda x:(x[2],-x[1],x[1]))
print(shop)
t = True
for i in range(1,len(shop)):
    if shop[i][2] != shop[i-1][2]:
        t = False

if t:
    mid = N//2
    for i in range(len(people)):
        tmp = 1e9
        chicken = abs(people[i][0] - shop[mid][0]) + abs(people[i][1] - shop[mid][1])
        tmp = min(tmp,chicken)
        total.append(tmp)
    print(sum(total))
else:
    for i in range(len(people)):
        tmp = 1e9
        chicken = 0
        for j in range(M):
            chicken = abs(people[i][0] - shop[j][0]) + abs(people[i][1] - shop[j][1])
            tmp = min(tmp,chicken)
            print(tmp,end=" ")
        total.append(tmp)
    print()
    print(total)
    print(sum(total))

