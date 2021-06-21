def solution(nums):
    #answer = 0
    board = []
    result = len(nums)//2
    for i in nums:
        if i not in board:
            board.append(i)
        
    if len(board) > result:
        return result
    else:
        return len(board)
    
    #return answer