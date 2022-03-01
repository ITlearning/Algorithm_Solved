# 전화번호 목록

# 테스트 케이스
t = int(input())

for _ in range(t):
    n = int(input())
    board = [input() for _ in range(n)]
    board.sort()
    flag = False
    for i in range(n-1):
        check = len(board[i])
        if board[i] == board[i+1][:check]:
            flag = True
    
    if flag:
        print("NO")
    else:
        print("YES")


