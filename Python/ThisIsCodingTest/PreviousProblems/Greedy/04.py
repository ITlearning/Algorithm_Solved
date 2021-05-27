# 만들 수 없는 금액

# 내 풀이
'''
n = int(input())

board = list(map(int,input().split()))

board.sort()

tmp = board[0]

if tmp > 1 :
    print('1')
else:
    for i in board[1:len(board)-1]:
        tmp += i
    print(tmp+1)
'''

# 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)