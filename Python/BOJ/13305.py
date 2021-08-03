# 주유소
# 각 도시에 있는 주유소의 기름 가격과, 
# 각 도시를 연결하는 도로의 길이를 입력으로 받아 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline
N = int(input())
road = list(map(int,input().split()))
location = list(map(int,input().split()))

# 제일 왼쪽 도시에서 그 다음 도시로 이동하려면 처음에는 처음도시 기름값으로 도로길이만큼 넣어야 한다.
total = road[0]*location[0]
# 그리고 일단 기름값이 제일 싼건 0번째 인덱스일테다. (아직 0번째니까)
small = location[0]
tmp = 0

for i in range(1,N-1):
    # 리터당 가격이 미리 정해놓은 제일 싼 가격보다 작을 경우
    if location[i] < small:
        total += small*tmp  # 제일 싼 가격 * 지금까지 이동한 거리(작은게 아닐경우 계속 움직였던 것)
        tmp = road[i]       # 현재 이동거리로 변경
        small = location[i] # 제일 싼 가격은 다시 갱신
    # 리터당 가격이 미리 정해놓은 제일 싼 가격보다 클 경우
    else:
        tmp += road[i]      # 이동거리 더해준다. (제일 싼곳에서 다 해먹어야 하기 때문에)

    # 도착지점 이전의 인덱스일 경우
    # ex) 5 2 [4] 1
    if i == N-2:
        # 전체 가격 += (지금까지 이동한 거리 * 제일 싼 리터당 가격)
        total += tmp*small

print(total)

# 사실 잘 이해하지 못함.. ㅠㅠ