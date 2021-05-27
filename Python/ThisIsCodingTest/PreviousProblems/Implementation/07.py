# 럭키 스트레이트

n = input()

board = []
for i in n:
    board.append(int(i))

if len(n) % 2 != 0 :
    print("READY")
else :
    half = (len(n) // 2)
    one = sum(board[:half])
    two = sum(board[half:])
    #print(one)
    if one == two :
        print("LUCKY")
    else :
        print("READY")