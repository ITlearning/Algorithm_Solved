# 에디터
from collections import deque
import sys
input = sys.stdin.readline
text = input().rstrip()

d = int(input())
left = deque()
for i in text:
    left.append(i)
right = deque()

cnt = 0

while d:
    a = input().split()
    if a[0] == "P":
        left.append(a[1])
    elif a[0] == "L":
        if left:
            right.appendleft(left.pop())
    elif a[0] == "D":
        if right:
            left.append(right.popleft())
    elif a[0] == "B":
        if left:
            left.pop()
    d -= 1

if right:
    left += right
    print("".join(left))
else:
    print("".join(left))

