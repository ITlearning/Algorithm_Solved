# 괄호의 값
import sys
input = sys.stdin.readline
problem = list(input().rstrip())
number = 1
total = 0
array = []
t = False
for i in range(len(problem)):
    if problem[i] =='(':
        array.append(problem[i])
        number *= 2
    elif problem[i] == '[':
        array.append(problem[i])
        number *= 3
    elif problem[i] == ']':
        if len(array) == 0 or array[-1] == '(':
            t = True
            break
        
        if problem[i-1] == '[':
            total += number
        array.pop()
        number //= 3
    elif problem[i] == ')':
        if len(array) == 0 or array[-1] == '[':
            t = True
            break

        if problem[i-1] == '(':
            total += number
        array.pop()
        number //= 2

if t or len(array):
    print(0)
else:
    print(total)
    