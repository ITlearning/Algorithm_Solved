# https://codedrive.tistory.com/54
import heapq

def solution(operations):
    answer = []
    for i in operations:
        a,b = i.split()
        if a == 'I':
            heapq.heappush(answer, int(b))
        else:
            if len(answer) > 0:
                if b == '1':
                    answer.pop(answer.index(heapq.nlargest( 1,answer)[0])) 
                    # nlargest : n개의 가장 큰 값들로 이루어진 리스트
                    # 첫번째 인자에 찾고싶은 최대값의 개수를 넣어주면 된다.
                else:
                    heapq.heappop(answer)
                    
    if len(answer) == 0:
        return [0,0]
    else:
        return [heapq.nlargest(1,answer)[0], answer[0]]