def solution(n, words):
    answer = []
    player = []
    word = []
    for i in range(1,n+1):
        player.append([i,0])
        
    i = 0
    T = True
    while i < len(words)-1:
        tmp = words[i]
        if words[i+1] not in word:
            word.append(tmp)
            if tmp[-1] != words[i+1][0]:
                i += 1
                player[i%n][1] += 1
                T = False
                break
            else:
                player[i%n][1] += 1
        else:
            i += 1
            player[i%n][1] += 1
            T = False
            break
        i += 1

    if T == True:
        answer = [0,0]
    else:
        answer = [player[i%n][0], player[i%n][1]]
    return answer