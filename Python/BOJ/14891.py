# 톱니바퀴
gear = []
for _ in range(4):
    tmp = map(int,input())
    gear.append(list(tmp))
k = int(input())

# 방향대로 돌리기
# 리스트 그대로 사용
def rotate(x, dir):
    if dir == 1:
        gear[x].insert(0, gear[x].pop())
    elif dir == -1:
        gear[x].append(gear[x].pop(0))

# k 번 돌아가면서 돌려야 할 톱니바퀴 위치와 방향 저장
for i in range(k):
    number, direction = map(int,input().split()) # 입력 받고
    dist = [[number-1, direction]] # 리스트에 저장
    z = direction
    x = number -1
    # 오른쪽부터 스캔
    while x+1 <= 3: 
        if gear[x][2] != gear[x+1][6]: # 맞물리는 곳이 다르다면
            z = -z
            dist.append([x+1, z]) # 돌려야할 것 업데이트 해줌 
            # 원래 코드에서 이 부분이 많이 막혔었음. 
            # while 문을 돌면서 하나하나 돌려야 하지만, 전 코드는 돌릴때 이미 돌린것도 같이 돌리다보니 값이 이상해짐
        else: # 같으면 종료
            break
        x += 1
    # 남은 왼쪽도 스캔
    x = number-1
    z = direction
    while x -1 >= 0:
        if gear[x][6] != gear[x-1][2]: # 방법은 동일. 단, 확인하는 맞물림 부분이 반대임
            z = -z
            dist.append([x-1, z]) # 돌려야 할 것 저장
        else:
            break
        x -= 1
    
    for x, dir in dist: # 그리고 여기서 돌릴거 보내준다.
        rotate(x,dir)


# 12시 방향 숫자들 확인해서 합한다.
result = (gear[0][0] * 1) + (gear[1][0] * 2) + (gear[2][0] * 4) + (gear[3][0] * 8)
# 답 도출
print(result)

# 소요시간 : 최소 3~4 시간. (며칠 지나긴 했음. . . )