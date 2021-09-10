from collections import deque

def solution(m, n, board):
    answer = 0
    #tmp = list(zip(*board[::1]))
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    d = 0
    while d != 1:
        dist = [[0]*n for i in range(m)]
        for i in dist:
            print(i)
        #print(d)
        t = True

        for i in range(m):
            for j in range(n):
                if board[i][j] == '0' or dist[i][j] == 1:
                    continue
                dist[i][j] = 1
                q = deque()
                q.append([i,j])
                cnt = 1
                current_x = 0
                current_y = 0
                default = board[i][j]
                print(default)
                while q:
                    print(q)
                    x,y = q.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        if dist[nx][ny] == 1 or board[nx][ny] != default:
                            continue
                        print("HIT")
                        dist[nx][ny] = 1
                        cnt += 1
                        q.append([nx,ny])
                if cnt >= 4:
                    print("Hello")
                    print(cnt)
                    answer += cnt
                    
                #else:
                
                #print()
        d += 1
        if d == 1:
            break

    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

