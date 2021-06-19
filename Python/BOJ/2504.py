# 괄호의 값
import sys
input = sys.stdin.readline
board = list(input().rstrip())
stack = []
circle = []
box = []
tmp = 1
result = 0
t = False

for i in range(len(board)):
    if board[i] == '[':
        stack.append(board[i])
        tmp *= 3
    elif board[i] == '(':
        stack.append(board[i])
        tmp *= 2
    elif board[i] == ')':
        if len(stack) == 0 or stack[-1] == '[' :
            t = True
            break

        if board[i-1] == '(':
            result += tmp
        stack.pop()
        tmp //= 2
    elif board[i] == ']':
        if len(stack) == 0 or stack[-1] == '(' :
            t = True
            break 
        if board[i-1] == '[':
            result += tmp
        stack.pop()
        tmp //= 3
if t or len(stack):
    print(0)
else:
    print(result)
    