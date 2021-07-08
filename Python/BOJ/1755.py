# 숫자놀이
import sys
input = sys.stdin.readline
# 각 숫자들의 문자들 리스트
alphabet = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# 숫자와 문자 한번에 저장하는 리스트
board = []

n,m = map(int,input().split())

# board 리스트에 숫자와 그 숫자에 해당하는 문자열 같이 저장하는 for 문
for i in range(n, m+1):
    tmp = ""        # 숫자가 10 이상일 경우 저장할 문자열
    if i >= 10:     # 10 이상일 경우
        t = str(i)  # 문자열로 변환
        for j in t: # 하나씩 뜯어서 변환
            tmp += alphabet[int(j)] # tmp 에 저장
            tmp += " "
        board.append([i, tmp]) # 변환이 끝나면 board에 숫자와 같이 저장
    else: # 10보다 작을 경우
        board.append([i, alphabet[i]]) # 그냥 저장

board.sort(key=lambda x: x[1]) # 문자열을 기준으로 사전순 정렬

# 출력
for i in range(len(board)):
    if i % 10 == 0 and not i == 0: # 10씩 끊어서 줄 넘기고 출력
        print()
        print(board[i][0], end=' ')
    else:
        print(board[i][0], end=' ')