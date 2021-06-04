# 그룹 단어 체커
t = int(input())
cnt = 0
for _ in range(t):
    t = True
    alpha = [False] * 26
    text = input()
    for i in range(len(text)):
        if alpha[int(ord(text[i]) - ord('a'))] == False:
            alpha[int(ord(text[i]) - ord('a'))] = True
        elif alpha[int(ord(text[i]) - ord('a'))] == True:
            if text[i] == text[i-1]:
                continue
            else:
                t = False
    if t:
        cnt += 1


print(cnt)