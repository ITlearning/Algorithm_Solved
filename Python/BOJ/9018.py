# 단어 맞추기
t = int(input())
board = []
for _ in range(t):
    tmp = input()
    board.append(list(tmp))

# 단어 맞추기 함수
def permutation(text):
    # 각각 제일 뒤보다 한 칸 앞
    left = len(text) - 2
    # 제일 뒤
    right = len(text) - 1

    # 뒤에서부터 돌면서 커지다가 작아지는 부분의 인덱스 추출
    for l in range(len(text)-1, 0, -1):
        if text[l] <= text[l-1]:
            left -= 1
        else:
            break

    # 돌렸는데 그런게 없으면 그냥 text출력
    if left == -1:
        return "".join(text)
    
    # 찾은 인덱스보다 커지는 숫자 출력
    for j in range(len(text)-1, -1, -1):
        if text[left] >= text[j]:
            right -= 1
        else:
            break

    # 그거 바꾸기
    text[left], text[right] = text[right], text[left]
    # 왼쪽, 오른쪽으로 나눠서 오른쪽만 sort
    answer = text[:left+1]
    right_sort = sorted(text[left+1:])
    answer.extend(list(right_sort))

    return "".join(answer)


for i in board:
    text = permutation(i)
    print(text)