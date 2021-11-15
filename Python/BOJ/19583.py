# 개강총회
import sys
input = sys.stdin.readline
S,E,Q = input().split()

S = S.split(":")
S = int("".join(S))

E = E.split(":")
E = int("".join(E))

Q = Q.split(":")
Q = int("".join(Q))

board = {}
check = []
cnt = 0
while True:
    try:
        time, nick_name = input().split()
        time = time.split(":")
        time = int("".join(time))
        #print(time, E)
        if time <= S or nick_name not in board:
            board[nick_name] = time
        else:
            #print(board[nick_name], S)
            if board[nick_name] <= S:
                if E <= time <= Q and nick_name not in check:
                    check.append(nick_name)
                    cnt += 1
    except:
        break

print(cnt)