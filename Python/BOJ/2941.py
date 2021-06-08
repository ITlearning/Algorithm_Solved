# 크로아티아 알파벳

cAlphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
dAl = ["c", "d", "l", "n", "s", "z"]
op = ["-","="]

text = input()
tmp = ""
cnt = 0
i = 0
while i < len(text):
    tmp += text[i]
    if tmp in op:
        tmp = ""
        i += 1
        if tmp in dAl:
        i += 1
        tmp += text[i]
            if tmp in cAlphabet:
                cnt += 1
                tmp = ""
            tmp += text[i]
            if tmp in cAlphabet:
                cnt += 1
                tmp = ""
    else:
        cnt += 1
        tmp = ""

print(cnt)