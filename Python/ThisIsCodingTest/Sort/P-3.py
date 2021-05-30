n,m = map(int, input().split())
boardA = list(map(int, input().split()))
boardB = list(map(int, input().split()))

boardA.sort()
boardB.sort(reverse=True)

for i in range(m):
    if boardA[i] < boardB[i]:
        boardA[i], boardB[i] = boardB[i], boardA[i]
    else:
        break


print(sum(boardA))