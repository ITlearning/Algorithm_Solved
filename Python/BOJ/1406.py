# 에디터

text = input()
n = int(input())
cursor = 0
for i in range(n) :
    con = input()
    if con == "L" :
        if cursor >= 0 :
            cursor += 1
    elif con == "D" :
        if cursor <= len(text) - 1 :
            cursor -= 1
    elif con == "B" :
        text.replace(text[cursor], "")
        cursor -= 1
        #if cursor != 0 :
            
    elif con == "P" :
        t = input()
        text.replace(text[cursor-1], t)

print(text)