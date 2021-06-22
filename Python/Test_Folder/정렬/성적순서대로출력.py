N = int(input())

board = []
for i in range(N):
    name, grade = input().split()
    board.append([name, grade])

board.sort(key=lambda x: x[1])

for i in board:
    print(i[0], end=' ')