# 탑
import sys
input = sys.stdin.readline

n = int(input())

tower = list(map(int,input().split()))
stack = []
laser = [0] * n

# 주어진 탑의 위치가 다음과 같으면
# 1 3 5 t . . 
# 현재 탑의 높이인 t가 5보다 작다면 5에서 수신을 할 것이기 때문에
# 1,3의 높이 정보는 알 필요가 없다.

# 따라서 오른쪽으로 이동하면서 하나씩 탑을 볼 때 
# 자신이 수신될 수 있는 탑의 위치를 찾을 때 이전의 탑의 높이가 현재 탑의 높이보다 작다면 버리면 되는 것이다.

for i in range(n):
    tmp = tower[i]
    while stack and tower[stack[-1]] < tmp:
        # 계속 뽑아준다.
        stack.pop()
    if stack:
        laser[i] = stack[-1] + 1
        
    stack.append(i)

print(*laser)