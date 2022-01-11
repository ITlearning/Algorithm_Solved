# 외계인의 기타연주
import sys
input = sys.stdin.readline
guitar = [[] for _ in range(7)]

n,m = map(int,input().split())
cnt = 0
for _ in range(n):
    jul, fret = map(int,input().split())

    # 입력받은 줄의 이미 누른 손이 있으면
    if len(guitar[jul]) != 0:
        # 제일 마지막에 누른 손이 입력받은 프렛보다 크다면
        if guitar[jul][-1] > fret:
            while True:
                guitar[jul].pop()
                cnt += 1
                # 만일 뽑고 난 뒤에 누른 손이 0개가 됐다면
                if len(guitar[jul]) == 0:
                    # 입력받은 프렛 넣고 카운트
                    guitar[jul].append(fret)
                    cnt += 1
                # 입력받은 프렛이 마지막 숫자보다 크면
                if guitar[jul][-1] < fret:
                    # 입력받은 프렛 넣고 카운트
                    guitar[jul].append(fret)
                    cnt += 1
                    break
                # 입력받은 프렛과 마지막 누른 숫자가 같으면
                elif guitar[jul][-1] == fret:
                    # while 문 종료
                    break
        # 입력받은 프렛과 마지막 누른 프렛 같으면
        elif guitar[jul][-1] == fret:
            # 넘어가기
            continue
        else: # 제일 마지막에 누른 손이 입력받은 프렛보다 작다면
            # 프렛 추가하고 카운트 증가
            guitar[jul].append(fret)
            cnt += 1
    else: # 줄에 누른손이 아무것도 없으면
        # 프렛 추가하고 카운트 증가
        guitar[jul].append(fret)
        cnt += 1


print(cnt)