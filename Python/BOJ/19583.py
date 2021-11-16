# 개강총회
import sys
input = sys.stdin.readline
S,E,Q = input().split()

# 입력받은 S,E,Q 숫자로만 분리
S = S.split(":")
S = int("".join(S))

E = E.split(":")
E = int("".join(E))

Q = Q.split(":")
Q = int("".join(Q))

board = {}  # 입력받은 유저를 저장할 딕셔너리
check = []  # 출석 체크 끝난 사람들 들어갈 리스트
cnt = 0
while True:
    try:  # try, except는 EOF 입력시 종료하는 조건을 만들기 위해 사용
        time, nick_name = input().split()  # 채팅 시간, 채팅자 입력받기
        
        # 숫자로 변경
        time = time.split(":")
        time = int("".join(time))

        # 입력받은 수가 개총 시작 전이거나, 딕셔너리에 존재하지 않는다면
        if time <= S or nick_name not in board:
            # 딕셔너리에 추가해줌
            board[nick_name] = time
        else:  # 그게 아니고 개총 시작 후거나, 딕셔너리에 존재하면
            if board[nick_name] <= S:  # 딕셔너리에 저장한 시간이 개총 시작 전이였다면
                if E <= time <= Q and nick_name not in check:  # 지금 입력받은 시간이 정상적으로 개총 종료 시간과
                                                               # 실시간 방송 종료 시간 사이에 이루어졌고, 이미
                                                               # 체크가 된 사람이 아니면 체크에 추가하고 카운트 증가
                    check.append(nick_name)
                    cnt += 1
    except:  # 그냥 엔터 누르면 이거 실행됨
        break

print(cnt)  # 답 도출