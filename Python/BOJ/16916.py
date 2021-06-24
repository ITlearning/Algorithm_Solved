# 부분 문자열
import sys
input = sys.stdin.readline
text = input()
pat = input()
text_len = len(text)
i = 0
pat_len = len(pat)
j = 0
cnt = 0
while i < len(text):
    if text[i] != pat[j]:
        i += 1
        j = 0
        continue
    elif text[i] == pat[j]:
        i += 1
        j += 1
        cnt += 1
        if cnt == pat_len:
            print(1)
            break

if cnt < pat_len:
    print(0)