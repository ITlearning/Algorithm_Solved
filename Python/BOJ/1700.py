# 멀티탭 스케줄링
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
board = list(map(int,input().split()))
plug = []
answer = 0

def check(i):
    # 앞으로 안쓰이는 것이면 뽑는다.
    # 모드 쓰이는 거라면 가장 나중에 쓰이는 것을 뽑는다.
    target = 0
    idx = -1
    for p in plug:
        # 이후에 쓰이지 않는거면 그냥 빼버리기
        if p not in board[i:]:
            return p
        if idx < board[i:].index(p):
            target = p
            idx = board[i:].index(p)
    return target

for i in range(k):
    if len(plug) < n:
        # 자리가 있고 원래 꼽았던게 들어올 경우
        if board[i] in plug:
            continue # 넘기기
        plug.append(board[i])
        continue
    # 자리가 다 찼고, 다른걸꼽아야 하는 상황
    if board[i] not in plug:
        plug[plug.index(check(i))] = board[i]
        answer += 1
print(answer)
