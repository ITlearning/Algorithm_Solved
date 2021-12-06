# 안테나

n = int(input())

board = list(map(int,input().split()))
max_len = max(board)

board.sort()

print(board[(n-1) // 2])