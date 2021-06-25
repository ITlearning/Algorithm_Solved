def solution(numbers, hand):
    answer = ''
    board = [[1,2,3],
             [4,5,6], 
             [7,8,9], 
             [10,0,11]]
    l = [3,0]
    r = [3,2]
    target = [0,0]
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            for i in range(len(board)):
                if number in board[i]:
                    l = [i,board[i].index(number)]
                    answer += "L"
                    continue
        elif number == 3 or number == 6 or number == 9:
            for i in range(len(board)):
                if number in board[i]:
                    r = [i,board[i].index(number)]
                    answer += "R"
                    continue
        else:
            for i in range(len(board)):
                if number in board[i]:
                    target = [i,board[i].index(number)]
                    target_L = abs(target[0]-l[0]) + abs(target[1]-l[1])
                    target_R = abs(target[0]-r[0]) + abs(target[1]-r[1])
                    
                    if target_L == target_R:
                        if hand == "left":
                            l = [target[0], target[1]]
                            answer += "L"
                        else:
                            r = [target[0], target[1]]
                            answer += "R"
                    else:
                        if target_L < target_R:
                            l = [target[0], target[1]]
                            answer += "L"
                        else:
                            r = [target[0], target[1]]
                            answer += "R"
    return answer