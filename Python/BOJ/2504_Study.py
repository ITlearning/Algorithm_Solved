# 괄호의 값
import sys
input = sys.stdin.readline
problem = list(input().rstrip())
number = 1
total = 0
array = []
t = False

# ex) ( ( ) [ [  ] ] ) ( [ ] )
#     2 4 2 6 18 6 2 1 2 6 2 1
#       +      +         +
# 4 + 18 + 6 = 28

# 결국 괄호마다 따로 곱해서 더해주고 이런방식이 아니라,
# 그냥 괄호가 닫히는 위치에 따라서 지금까지 곱해준걸 더해줘도 
# 어짜피 답은 나온다는 것이 결론.


# 입력받은 괄호 수 만큼 돌린다.
for i in range(len(problem)):
    # 괄호가 열린 소괄호면 
    if problem[i] =='(':
        # 리스트 추가
        array.append(problem[i])
        # 그리고 동시에 2 곱하기
        number *= 2
    elif problem[i] == '[':
        array.append(problem[i])
        # 3곱하기
        number *= 3
    elif problem[i] == ']':
        # 리스트레 추가 된 직전의 괄호가 짝이 맞지 않는 경우와, 아얘 없으면 종료
        if len(array) == 0 or array[-1] == '(':
            t = True
            break
        # 입력받은 괄호 중 지금 순서 바로 전 괄호가 짝이 맞는다면
        if problem[i-1] == '[':
            # 지금까지 곱했던거 더해주고
            total += number
        # 리스트 제거
        array.pop()
        number //= 3
    elif problem[i] == ')':
        if len(array) == 0 or array[-1] == '[':
            t = True
            break

        if problem[i-1] == '(':
            total += number
        array.pop()
        number //= 2

# 돌리는 중간에 괄호가 맞지 않았거나, 끝났어도 리스트에 뭔가가 남았을 경우
if t or len(array):
    print(0)
else: # 그게 아니고 정상적으로 괄호가 맞는다면
    print(total)
    