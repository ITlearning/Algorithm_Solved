# 시리얼 번호
# 시리얼번호 A가 시리얼번호 B의 앞에 오는 경우는 다음과 같다.

# 1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
# 2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
# 3. 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.

n = int(input())

board = []

for _ in range(n):
    board.append(input())

def plus_sum(text):
    number = 0
    for i in text:
        if i.isdigit():
            number += int(i)

    return number


board.sort(key=lambda x : (len(x), plus_sum(x), x))

for b in board:
    print(b)

