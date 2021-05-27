# 문자열 재정렬
s = input()
board = ""
s = sorted(s)
num = 0
for i in s:
    if int(ord(i)) < 65 :
        num += int(i)
    else:
        board += i

if num != 0 :
    board += str(num)

print(board)