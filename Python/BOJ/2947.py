# 나무조각

# 입력 받기
board = list(map(int,input().split()))

# 원하는 답의 모양 리스트
answer = [1,2,3,4,5]
while True:
    # 입력받은 board를 돌면서 
    for i in range(len(board)-1):
        # 그 다음 수보다 클 경우
        if board[i] > board[i+1]:
            # 위치 변경 하고
            board[i], board[i+1] = board[i+1], board[i]
            # 전체 board 출력
            print(*board)
    
    # 바꾼 결과가 답과 일치하면 종료
    if board == answer:
        break
    # 아니면 다시 돌리기