# 고냥이
from collections import Counter
from collections import deque
n = int(input())

text = input()
answer = deque()
start = 0
end = n
for i in text[start:end-1]:
    answer.append(i)
print(answer)
while start <= end:
    answer.append(text[end])
    tmp = Counter(answer)
    if len(tmp) < n:
        end += 1
    else:
        start += 1

# 모르겠다..