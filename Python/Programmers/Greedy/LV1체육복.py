def solution(n, lost, reserve):
    # 인원수가 안맞다는 거네?
    lost.sort()
    reserve.sort()
    
    cnt = n - len(lost)
    new_lost = []
    for i in lost:
        new_lost.append(i)
        if i in reserve:
            cnt += 1
            new_lost.remove(i)
            #lost.remove(i)
            reserve.remove(i)
            
    for a in new_lost:
        if a-1 in reserve:
            cnt += 1
            reserve.remove(a-1)
        elif a+1 in reserve:
            cnt += 1
            reserve.remove(a+1)
            
    return cnt

# 풀이: lost를 삭제하지 않은 상태로 아래 for문을 돌경우
# 원래는 지워져야했던 숫자가 개수 세는 것에 영향을 줌.
# 따라서 새로운 리스트를 파 new_lost를 만들어
# 바꿔진 lost의 수만으로 나머지 개수들을 파악