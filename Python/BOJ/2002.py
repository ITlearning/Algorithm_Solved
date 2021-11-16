# 추월
n = int(input())
board = {}

# 딕셔너리에 key를 입력받은 차 번호로, value를 순서로 저장
for i in range(1,n+1):
    board[input()] = i

min_num = min(board.values())  # 딕셔너리 중에서 제일 순서가 작은 숫자
cnt = 0

for _ in range(n):
    tmp = input()  # 입력받기
    if min_num != board[tmp]:  # 입력받은 차번호에 대해서 순서가 제일 작은 숫자와 다르다면
        cnt += 1  # 추월한 차량으로 인식되니 카운트 증가
        del board[tmp]  # 차량 지우기
    else:  # 그게 아니고 같다면
        del board[tmp]  # 제대로 나온 것이니 그냥 지워주기
        if board:  # 아직 차량이 남아 있으면
            min_num = min(board.values())  # 지금 남아있는 차량 중에 작은 숫자 갱신

print(cnt)