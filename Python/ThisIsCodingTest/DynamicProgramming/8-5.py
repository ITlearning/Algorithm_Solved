# 1로 만들기

x = int(input())

d = [0] * 30001
# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2,x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    if i%2 == 0: # 2로 나눠질경우
        d[i] = min(d[i], d[i//2] +1)
    if i%3 == 0: # 3으로 나눠질경우
        d[i] = min(d[i], d[i//3] +1)
    if i%5 == 0: # 5로 나눠질경우
        d[i] = min(d[i], d[i//5] +1)

print(d[x])