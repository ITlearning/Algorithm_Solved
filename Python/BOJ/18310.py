# 안테나

n = int(input())

# board 입력받기
board = list(map(int,input().split()))

# 정렬
# 제일 적은 거리의 총 합을 구할 수 있는 곳은 정렬된 곳의 중앙이기 때문에
# 정렬 후 가운데의 인덱스를 뽑아내면 됨
board.sort()

print(board[(n-1) // 2])