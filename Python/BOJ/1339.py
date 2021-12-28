# 단어 수학

n = int(input())

board = []
answer_dic = {}
for _ in range(n):
    board.append(input())

# 입력받은 텍스트 하나씩 꺼내면서 체크
for text in board:
    # 인덱스와 알파벳을 하나씩 꺼냄
    for index,alphabet in  enumerate(text):
        # 만일 알파벳이 딕셔너리에 존재하지 않으면
        if alphabet not in answer_dic:
            # 그 위치의 크기(예를 들자면 ACGFE 라는 문자에서 A의 위치의 크기는(5 - 0 - 1)(0의 개수) 10000) 를 계산해서 추가   
            answer_dic[alphabet] = 10 ** (len(text) - index - 1)
        else:
            # 이미 있으면 그냥 그 숫자에서 더 추가
            answer_dic[alphabet] += 10 ** (len(text) - index - 1)

# 계산한 value 값으로 크기가 큰 순서대로 정렬
answer_list = sorted(answer_dic.items(), key=lambda x : x[1], reverse=True)

answer = 0
cnt = 9
# 정렬된 리스트의 숫자에 9,8,7..이렇게 곱해줌
for num in answer_list:
    answer += num[1] * cnt
    cnt -= 1

# 답 도출
print(answer)