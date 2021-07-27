# 치킨 배달
from itertools import combinations
N,M = map(int,input().split())

board = []
people = []
shop = []
# 리스트에 일단 다 추가
for i in range(N):
    board.append(list(map(int,input().split())))


# 그리고 치킨집 따로, 집 따로 위치 각각 리스트에 저장
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            people.append([i+1,j+1])
        elif board[i][j] == 2:
            shop.append([i+1,j+1])

k = 0
small = []

# 먼저 입력했던 최대 치킨집 수를 기준으로 조합을 내어 리스트에 저장
brute = list(combinations(shop,M))

# 조합을 돌면서 최솟값 구하기
for permution in brute:
    total = 0
    for p in people:
        tmp = []
        for i in permution:
            tmp.append(abs(i[0]-p[0]) + abs(i[1]-p[1]))
        # 오름차순 정렬을 통해 제일 적은 거리 도출
        tmp.sort()
        total += tmp[0]
    # 그리고 small 리스트에 다 저장
    small.append(total)

# 모든 합에서 제일 작은거 뽑아서 답으로 도출
small.sort()
print(small[0])

