# 스타트와 링크
from itertools import combinations
n = int(input())
board = []
# 입력받은 n 만큼의 숫자가 있는 check리스트
check = [i for i in range(n)]

# 입력받기
for _ in range(n):
    board.append(list(map(int,input().split())))

answer = 99999999999

# 팀의 조합을 짜주는 for문
# 아까 만들었던 check리스트로 스타트팀과 링크팀의 번호를 지정
for start_combi in combinations(check, n//2):
    start = 0
    link = 0
    # 만일 start_combi가 1,2 이면 나머지 팀을 꾸릴 수 있는 숫자인 0,3을 link_combi로 지정
    link_combi = list(set(check)-set(start_combi))

    # 짜여진 팀 숫자로 점수 따져보기
    for s in combinations(start_combi, 2):
        start += board[s[0]][s[1]]
        start += board[s[1]][s[0]]

    for l in combinations(link_combi, 2):
        link += board[l[0]][l[1]]
        link += board[l[1]][l[0]]
    
    # 계산해서 나온 숫자의 차이가 작다면 갱신
    answer = min(answer, abs(start - link))

print(answer)