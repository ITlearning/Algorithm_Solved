# 크리스마스 선물
import heapq

n = int(input())
q = []

# 입력받은 n만큼 돌리기
for _ in range(n):
    a = list(map(int,input().split()))
    
    # 입력받은 수가 0이 아니면
    if a[0] != 0:
        # 0 이후의 숫자 가져와서 입력(우선순위큐에 순서를 반대로)
        numbers = a[1:]
        for number in numbers:
            heapq.heappush(q, -number)
    else:
        # 0 을 입력받았으면
        if q:
            # 우선순위 큐에 의해 제일 우선순위가 높은 숫자부터 빠짐
            print_num = heapq.heappop(q)
            # 저장된게 -로 저장되어있으니 출력은 다시 - 해주고
            print(-print_num)
        else:
            # 애초에 큐에 없으면 -1 출력
            print(-1)
