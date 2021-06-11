def solution(n, times):
    answer = 0
    # 최솟값 = 0 또는 1
    start = 0
    # 최댓값 = 가장 늦게 처리해주는 심사관에게 다 받았을 최악의 경우
    end = max(times) * n
    
    # 최솟값이 최대값과 같거나 클 경우 종료
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        # 매 턴마다 중간값으로 설정했을때 심사관들이 처리할 수 있는 인원들에 대해 계산
        for time in times:
            cnt += mid//time
            # 만일 도중에 가능한 인원수를 넘어섰을 경우에 중지
            if cnt >= n:
                break

        # 가능한 인원이 원래 심사받아야할 인원들과 같거나 많을 경우 처리가 가능한 것
        if cnt >= n:
            # 답으로 설정을 해두고
            answer = mid
            # 최대값을 하나 빼주고 다시 시작
            end = mid-1
        # 가능한 인원이 받아야 할 인원수 보다 적을 경우
        elif cnt < n:
            # 최소값을 하나 더하고 다시 시작
            start = mid+1
        
    return answer