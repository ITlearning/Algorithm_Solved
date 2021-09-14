from collections import deque

def solution(m, n, board):
    answer = 0
    set_check = set()
    board = list(map(list, board)) # 입력받은 board 문자열 리스트로 나누기

    # 2X2 체크 함수
    def check(board):
        for i in range(m-1):
            for j in range(n-1):
                # 돌면서 2X2 규격에 맞다면 세트에 추가 (세트는 중복을 추가하지 않기 때문에 같은 수가 나오더라도 추가 안함)
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != '0':
                    set_check.add((i,j))
                    set_check.add((i+1,j))
                    set_check.add((i,j+1))
                    set_check.add((i+1,j+1))

    # 배열 내려주기
    def update(board):
        # 덱을 이용
        q = deque()
        for i in range(len(board[0])):
            for j in range(len(board)-1,-1,-1):
                # 각 열을 세로로 돌면서 0이 나왔을경우에는 덱에 추가해주고
                if board[j][i] == '0':
                    q.append([j,i])
                # 알파벳이 나오면 그 자리랑 0 자리랑 교체
                else:
                    if len(q) != 0:
                        x,y = q.popleft()
                        board[x][y], board[j][i] = board[j][i], board[x][y]
                        # 이 때, 바뀐 그 자리도 0 위치이므로 덱에 같이 추가해준다.
                        q.append([j,i])
            # 만일 0위치가 다 위쪽이면 어짜피 교체 안해도 되니 덱에 있는 거 다 지움
            q.clear()
    
    while True:
        # 체크 함수
        check(board)

        # 체크해서 2X2 규격의 것이 있으면
        if len(set_check) != 0:
            # 일단 다 0으로 바꿔주고
            for i, j in set_check:
                board[i][j] = '0'
            # 답에 set에 있는 개수 추가해주고
            answer += len(set_check)
            # 배열 내리기
            update(board)
            # 그리고 set에 존재했던 것들 다 지워주기
            set_check.clear()
        # 지워질게 없으면 종료
        else:
            break

    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

