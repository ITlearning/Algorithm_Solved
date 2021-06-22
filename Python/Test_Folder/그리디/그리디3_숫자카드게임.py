# 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
N,M = map(int,input().split())
board = []
big = -1
for _ in range(N):
    text = list(map(int,input().split()))
    small = min(text)
    big = max(big, small)

print(big)