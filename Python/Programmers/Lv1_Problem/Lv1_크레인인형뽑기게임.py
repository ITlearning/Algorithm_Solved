def solution(board, moves):
    answer = 0
    N = len(board)
    box = []
    for move in moves:
        for j in range(0,N):
            if board[j][move-1] != 0:
                box.append(board[j][move-1])
                board[j][move-1] = 0
                break  
        if len(box) >= 2:
            if box[-2] == box[-1]:
                box.pop()
                box.pop()
                answer += 2
    return answer