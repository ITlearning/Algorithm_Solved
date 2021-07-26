# 톱니바퀴
gear = []
for _ in range(4):
    tmp = map(int,input())
    gear.append(list(tmp))
k = int(input())
board = gear[:]
for i in range(k):
    number, direction = map(int,input().split())
    number = number-1
    print("number:", number)
    left = number - 1
    right = number + 1
    while left > -1 and right < 4:
        print(gear[number][2] , gear[right][6])
        if gear[number][2] != gear[right][6]:
            if direction == 1:
                tmp = board[number].pop(0)
                board[number].append(tmp)

                tmp = board[right].pop()
                board[right].insert(0,tmp)
            elif direction == -1:
                tmp = board[number].pop(0)
                board[number].append(tmp)

                tmp = board[right].pop()
                board[right].insert(0,tmp)
            right += 1
            number += 1


        #if gear
        else:
            break

for i in gear:
    print(i)
print()

for j in board:
    print(j)