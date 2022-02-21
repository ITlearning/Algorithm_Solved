# 링

n = int(input())

board = list(map(int,input().split()))

def gcd(a,b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    
    return a


for i in range(1, len(board)):
    num = gcd(board[0], board[i])
    print("{0}/{1}".format(board[0] // num, board[i] // num))