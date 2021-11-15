from collections import deque

def check(board, circle, person):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O":
                circle.append([i,j])
            elif board[i][j] == "P":
                person.append([i,j])

def solution(places):
    answer = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for pl in places:
        board = []
        circle = deque()
        person = deque()
        for pj in pl:
            board.append(list(pj.rstrip()))
        
        check(board,circle, person)
        
        person_flag = True
        while person:
            x,y = person.popleft()
            for cur in range(4):
                nx = x + dx[cur]
                ny = y + dy[cur]
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == "P":
                        person_flag = False
                        break
            if not person_flag:
                break
        
        circle_flag = True   
        while circle:
            cx,cy = circle.popleft()
            cnt = 0
            for cur in range(4):
                nx = cx + dx[cur]
                ny = cy + dy[cur]
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == "P":
                        cnt += 1
            if cnt > 1:
                circle_flag = False
                break
                
        if person_flag and circle_flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer