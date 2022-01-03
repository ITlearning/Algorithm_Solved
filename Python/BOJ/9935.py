# 문자열 폭발
from copy import deepcopy
text = input()
tmp = deepcopy(text)
match_text = input().rstrip()
stack = []
for i in text:
    stack.append(i)
    if i == match_text[-1] and "".join(stack[-len(match_text):]) == match_text:
        for _ in range(len(match_text)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")