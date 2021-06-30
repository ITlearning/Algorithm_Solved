# IOIOI
import sys
input = sys.stdin.readline
N = int(input())
text_size = int(input())
text = input().rstrip()
i = 1
answer = 0
cnt = 0

while i < text_size-1:
    if text[i-1] == 'I' and text[i] == 'O' and text[i+1] == 'I':
        cnt += 1
        if cnt == N:
            cnt -= 1
            answer += 1
        i += 1
    else:
        cnt = 0
    i += 1

print(answer)