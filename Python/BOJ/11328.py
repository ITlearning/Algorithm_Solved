n = int(input())

for i in range(n) :
    t = True
    text ,retext= input().split()
    if len(text) != len(retext) :
        print("Impossible")
        continue

    text = sorted(text)
    retext = sorted(retext)
    for i in range(len(text)) :
        if text[i] != retext[i] :
            t = False
            break
        else :
            t = True
    
    if t:
        print("Possible")
    else :
        print("Impossible")