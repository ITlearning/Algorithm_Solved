# 괄호의 값
import sys
input = sys.stdin.readline
board = list(input().rstrip())
stack = []
tmp = 1
result = 0
impossible = False
print(board)
for i in range(len(board)):
    if board[i] == '(':
        stack.append(board[i])
        tmp *= 2
    elif board[i] == '[':
        stack.append(board[i])
        tmp *= 3
    elif board[i] == ')' and (stack[-1] != '(' or len(stack) == 0):
        impossible = True
        break
    elif board[i] == ']' and (stack[-1] != '[' or len(stack) == 0):
        impossible = True
        break
    elif board[i] == ']':
        if board[i-1] == '[':
            result += tmp
            
        tmp //= 3
    elif board[i] == ')':
        if board[i-1] == '(':
            result += tmp
        tmp //= 2


if impossible or len(stack) != 0:
    print(0)
else:
    print(result)