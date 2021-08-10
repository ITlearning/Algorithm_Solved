# 패션왕 신혜빈
from collections import Counter
T = int(input())

# 결론적으로 가지고 있는 것들로 몇가지의 조합을 얻어내는가에 대한 문제.

# 케이스 수까지 while문 돌림
while T > 0:
    board = []
    N = int(input())
    # 일단 입력받은 개수는 최소 개수일테니 먼저 더해주고
    total = N
    # for문 돌리면서 종류 개수를 구하기 위해 board리스트에 저장
    for i in range(N):
        stuff, category = map(str,input().split())
        board.append(category)
    
    # 그리고 각 종류의 개수를 구하고
    result = Counter(board)
    total = 1
    # 개수의 종류를 곱하며 +1개를 해준다.
    for i in result.values():
        total *= i+1
    
    # 아무것도 안입은 상태 1가지를 뺴주면 답 도출
    print(total - 1)
    T -= 1