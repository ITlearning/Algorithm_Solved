# 전화번호 목록

# 테스트 케이스
t = int(input())

for _ in range(t):
    n = int(input())
    board = [input() for _ in range(n)]
    # 정렬을 하면 길이가 짧은 순서대로 정렬된다.
    board.sort()
    flag = False

    for i in range(n-1):
        # 따라서 하나씩 돌려보며 작은 길이의 글자수 만큼 대조 해서 같으면 true 다르면 false 반환
        check = len(board[i])
        if board[i] == board[i+1][:check]:
            flag = True
    
    if flag:
        print("NO")
    else:
        print("YES")


