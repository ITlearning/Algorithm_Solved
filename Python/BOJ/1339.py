# 단어 수학

n = int(input())

board = []
answer_dic = {}
for _ in range(n):
    board.append(input())

for text in board:
    for index,alphabet in  enumerate(text):
        if alphabet not in answer_dic:
            answer_dic[alphabet] = 10 ** (len(text) - index - 1)
        else:
            answer_dic[alphabet] += 10 ** (len(text) - index - 1)

answer_list = sorted(answer_dic.items(), key=lambda x : x[1], reverse=True)

answer = 0
cnt = 9
for num in answer_list:
    answer += num[1] * cnt
    cnt -= 1

print(answer)