# 숫자놀이
import sys
input = sys.stdin.readline
alphabet = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
board = []
n,m = map(int,input().split())

for i in range(n, m+1):
    tmp = ""
    if i >= 10:
        t = str(i)
        for j in t:
            tmp += alphabet[int(j)]
            tmp += " "
        board.append([i, tmp])
    else:
        board.append([i, alphabet[i]])

board.sort(key=lambda x: x[1])
for i in range(len(board)):
    if i % 10 == 0 and not i == 0:
        print()
        print(board[i][0], end=' ')
    else:
        print(board[i][0], end=' ')