# 스택
import sys
input = sys.stdin.readline
stack = []
t = int(input())

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]

for _ in range(t):
    text = input().rstrip().split()
    if text[0] == "push":
        push(text[1])
    elif text[0] == "top":
        print(top())
    elif text[0] == "size":
        print(size())
    elif text[0] == "empty":
        print(empty())
    elif text[0] == "pop":
        print(pop())
