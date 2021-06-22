# 그리디 문제
# 문제에서의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 떄 주어진 수들을
# M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번
# 을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

# N 수의 총 개수,M 번 더하기 , K 번 연속해서 더하기
N,M,K = map(int,input().split())

board = list(map(int,input().split()))
board.sort()
answer = 0
for i in range(1,M+1):
    if i % K != 0:
        answer += board[-1]
    else:
        answer += board[-2]

print(answer)