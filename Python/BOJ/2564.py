# 경비원
n,m = map(int,input().split())

shop_cnt = int(input())
shop_list = []

for _ in range(shop_cnt):
    shop_radius, shop_distance = map(int,input().split())
    shop_list.append([shop_radius, shop_distance])

guard_man_radius, guard_man_distance = map(int,input().split())

answer = 0
for shop in shop_list:
    # 경비원과 매점의 위치가 같을 경우
    if shop[0] == guard_man_radius:
        answer += abs(shop[1] - guard_man_distance)
    else:  # 아닐 경우
        # 모든 경우의 수 다 따져봄..ㅠㅅ  ㅠ
        if shop[0] == 1:
            if guard_man_radius == 2:
                answer += min(shop[1]+m+guard_man_distance, (n-shop[1])+m+(n-guard_man_distance))
            elif guard_man_radius == 3:
                answer += min(shop[1]+guard_man_distance, (n-shop[1])+m+n+(m-guard_man_distance))
            elif guard_man_radius == 4:
                answer += min((n-shop[1])+guard_man_distance, shop[1]+m+n+(m-guard_man_distance))
        elif shop[0] == 2:
            if guard_man_radius == 1:
                answer += min(shop[1]+m+guard_man_distance, (n-shop[1])+m+(n-guard_man_distance))
            elif guard_man_radius == 3:
                answer += min(shop[1]+(m-guard_man_distance), (n-shop[1])+m+n+guard_man_distance)
            elif guard_man_radius == 4:
                answer += min((n-shop[1])+(m-guard_man_distance), shop[1]+m+n+guard_man_distance)
        elif shop[0] == 3:
            if guard_man_radius == 1:
                answer += min(shop[1]+guard_man_distance, (m-shop[1])+n+m+(n-guard_man_distance))
            elif guard_man_radius == 2:
                answer += min((m-shop[1])+guard_man_distance, shop[1]+n+m+(n-guard_man_distance))
            elif guard_man_radius == 4:
                answer += min(shop[1]+n+guard_man_distance, (m-shop[1])+n+(m-guard_man_distance))
        elif shop[0] == 4:
            if guard_man_radius == 1:
                answer += min(shop[1]+(n-guard_man_distance), (m-shop[1])+n+m+guard_man_distance)
            elif guard_man_radius == 2:
                answer += min((m-shop[1])+(n-guard_man_distance), shop[1]+n+m+guard_man_distance)
            elif guard_man_radius == 3:
                answer += min(shop[1]+n+guard_man_distance, (m-shop[1])+n+(m-guard_man_distance))

print(answer)
