# 카드 문자열

T = int(input())

while T > 0:
    N = int(input())
    board = list(map(str,input().split()))
    answer = [board[0]]
    for i in board[1:]:
        left = answer[0]
        if left >= i:
            answer.insert(0, i)
        else:
            answer.append(i)
    
    print("".join(answer))

    T -= 1