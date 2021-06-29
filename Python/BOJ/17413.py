# 단어 뒤집기 2
import sys
input = sys.stdin.readline
S = input().rstrip()
tmp = []
text = ""
result =""
tag = True
for i in S:
    if i == '<':
        tag = False
        result += text
        text = '<'
    elif i == '>':
        tag = True
        result += (text + '>')
        text = ''
    elif i == ' ':
        result += (text + ' ')
        text = ''
    elif tag:
        text = i + text
    else:
        text += i


print(result+text)



