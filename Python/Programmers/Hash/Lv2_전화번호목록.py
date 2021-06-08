from collections import deque

def solution(phone_book):
    answer = True
    phone_book.sort()
    q = []
    q = deque(q)
    q.append(str(phone_book[0]))
    for i in range(1,len(phone_book)):
        cur = q.popleft()
        q.append(str(phone_book[i]))
        if  str(phone_book[i]).startswith(cur) or str(phone_book[i]).endswith(cur,len(phone_book[i])):
            return False
            
        
    return answer