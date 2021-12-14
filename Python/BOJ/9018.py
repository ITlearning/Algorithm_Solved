# 단어 맞추기
from itertools import permutations
t = int(input())
board = []
for _ in range(t):
    tmp = input()
    board.append(list(tmp))

def permutation(text):
    left = len(text) - 2
    right = len(text) - 1

    for l in range(len(text)-1, 0, -1):
        if text[l] <= text[l-1]:
            left -= 1
        else:
            break

    if left == -1:
        return "".join(text)
    
    for j in range(len(text)-1, -1, -1):
        if text[left] >= text[j]:
            right -= 1
        else:
            break

    text[left], text[right] = text[right], text[left]
    answer = text[:left+1]
    right_sort = sorted(text[left+1:])
    answer.extend(list(right_sort))

    return "".join(answer)


for i in board:
    text = permutation(i)
    print(text)
