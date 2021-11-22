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
    if shop[0] == guard_man_radius:
        answer += abs(shop[1] - guard_man_distance)
    else:
        if shop[0] in [1,2]:
            if guard_man_radius in [1,2]:
                answer += min(abs(guard_man_distance + m + shop[1]), abs((n-guard_man_distance)+m+(n-shop[1])))
                print(min(abs(guard_man_distance + m + shop[1]), abs((n-guard_man_distance)+m+(n-shop[1]))))
            else:
                answer += min(abs((m-guard_man_distance)+ shop[1]), abs((guard_man_distance+n+m+shop[1])))
                print(min(abs(guard_man_distance + m + shop[1]), abs((n-guard_man_distance)+m+(n-shop[1]))))
        elif shop[0] in [3,4]:
            if guard_man_radius == 1:
                answer += min(shop)
            elif guard_man_radius == 2:
                answer += min((n - shop[1] + guard_man_distance, shop[1] + m + n + (m - guard_man_distance)))

print(answer)
