# 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
board = []

for i in range(N):
    tmp = list(map(int,input().split()))
    board.append(tmp)

# 종료시간이 빠른순, 같으면 시작 시간이 빠른순 정렬
board.sort(key= lambda x : (x[1], x[0]))

cnt = 0   # 최대 횟수 카운트
limit = 0 # 현재 돌아가는 카운트의 끝나는 초를 기록하는 변수

for time in board:
    # 만일 지금 뽑은 시간의 시작 시간이 입력된 최대 수를 넘었다면
    # 그건 돌릴 수 있는 회의실 사용 시간이니 if문 안으로 들어감
    if time[0] >= limit:
        cnt += 1
        limit = time[1]

print(cnt)