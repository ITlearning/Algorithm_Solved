# 마인크래프트
import sys

input = sys.stdin.readline

n,m,b = map(int,input().split())
INF = int(1e9)
board = []
# 시간을 저장해둘 변수, 값일 될 height
time, result_height = INF, 0

for _ in range(n):
    board.append(list(map(int,input().split())))

# 결과적으로 0부터 256까지의 높이를 계산 하면서 하나하나 따져보면 되는 것이다.
for height in range(257):
    bottom = 0
    top = 0
    for i in range(n):
        for j in range(m):
            # 따라서 현재 높이보다 지금 찾은 곳의 높이가 작다면
            if board[i][j] < height:
                # 그것은 답의 높이가 될 가능성이 존재하니, 식을 계산
                bottom += height-board[i][j]
            else:
                # 그게 아닐 경우에는
                # 반대로 계산
                top += board[i][j] - height
    
    # 다 계산 후
    # 지금 제일 작은 높이가 top + b의 계수보다 높을 경우
    # 계산을 할 필요가 없기에 넘아감
    if bottom > top + b:
        continue
    
    # 반대로 계산할 필요가 있을 경우에는
    # bottom과 제일 높은 크기의 숫자를 * 2하여 check_time을 만듬
    check_time = bottom + top * 2
    # 그리고 현재 시간과 체크한 시간을 비교해서 더 짧으면 
    if check_time <= time:
        # 갱신
        time = check_time
        result_height = height

# 마지막으로 출력
print(time, result_height)
    