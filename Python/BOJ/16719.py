# ZOAC

texts = list(input())

text_dic = []
answer = []
total = []

for index, text in enumerate(texts):
    text_dic.append([text, index])

sort_texts = sorted(text_dic, key= lambda x : x[0])

print(sort_texts)

for text in sort_texts:
    if len(answer) == 0:
        answer.append(text)
    elif len(answer) == 1 :
        if answer[0][1] < text[1]:
            answer.append(text)
        else:
            answer.insert(0, text)
    else:
        for t in range(len(answer)-1, -1,-1):
            if answer[t][1] > text[1] > answer[t-1][1]:
                answer.insert(t, text)
                break

            if t == 0:
                if text[1] < answer[0][1]:
                    answer.insert(0, text)
                else:
                    answer.append(text)
    tmp = ""
    
    for a in answer:
        tmp += a[0]
    
    total.append(tmp)

total.sort(key= lambda x : (len(x), x))

for t in total:
    print(t)

