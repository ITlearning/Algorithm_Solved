# 창고 다각형

# 기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n = int(input())
# 기둥 최대 개수 만큼 기둥의 크기를 저장할 리스트 생성
board = [0] * (1001)

max_number = -1 # 입력받은 수 중 가장 큰 수
max_index = 0   # 입력받은 수 중 가장 큰 수의 인덱스
end_index = 0   # 입력받은 기둥의 마지막 인덱스

# 1. 돌면서 하나씩 입력을 받으면서 가장 큰 수와 인덱스를 얻어낸다.
for i in range(n):
    l,h = map(int,input().split())
    if max_number < h:
        max_number = h
        max_index = l
    if end_index < l:
        end_index = l
    # 그와 무관하게 board에 입력받은 기둥의 정보를 입력
    board[l] = h

# 2. 가장 큰 기둥을 기준으로 왼쪽 오른쪽으로 나누어서 계산
# 각 부분에서 그 순간 가장 큰 수로 계속 더하기를 진행
left_max = -1  # 왼쪽 부분에서 가장 큰 수
left_total = 0 # 왼쪽 부분을 합한 수

# 2-1. 왼쪽 부분부터 돌기 시작
for i in range(max_index+1):
    # 가장 크다고 기록했던 기둥보다 더 큰 기둥일 경우
    if left_max < board[i]:
        # 기둥 갱신하고
        left_max = board[i]
        # 갱신한 값으로 더하기
        left_total += left_max
    else: # 그게 아니고 작을 경우
        # 가장 큰 수로 더해주기 board[i]
        left_total += left_max

# 2-2. 오른쪽 부분도 돌기 시작
# 오른쪽 부분은 반대 인덱스부터 돌아감
right_max = -1  # 오른쪽 부분에서 가장 큰 수
right_total = 0 # 오른쪽 부분을 합한 수

for j in range(end_index, max_index, -1):
    # 가장 크다고 기록했던 기둥보다 더 큰 기둥일 경우
    if right_max < board[j]:
        # 기둥 갱신
        right_max = board[j]
        # 더하기
        right_total += right_max
    else: # 작을 경우
        # 기존에 있던 기록으로 더하기
        right_total += right_max

# 3. 두개의 값을 더해서 출력
print(left_total + right_total)