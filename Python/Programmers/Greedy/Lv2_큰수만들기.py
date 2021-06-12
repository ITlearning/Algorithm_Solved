def solution(number, k):
    answer = ''
    cnt = 0
    num = list(number)
    board = [num[0]]
    
    for i in range(1, len(num)):
        if cnt == k:
            board = board + num[i:]
            break
        
        board.append(num[i])
        if board[-1] > board[-2]:
            while len(board) != 1 and (board[-1] > board[-2] and cnt < k):
                board[-1], board[-2] = board[-2], board[-1]
                board.pop()
                cnt += 1
    
    return "".join(board[:len(num)-k])