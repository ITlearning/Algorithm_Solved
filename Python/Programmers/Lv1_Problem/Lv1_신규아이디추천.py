def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    tmp = ""
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ('-','_','.'):
            tmp += i
    # 3단계
    while '..' in tmp:
        tmp = tmp.replace('..', '.')
    print(tmp)
    # 4단계
    tmp = tmp[1:] if tmp[0] == '.' and len(tmp) > 1 else tmp
    tmp = tmp[:-1] if tmp[-1] == '.' else tmp
    
    # 5단계
    if tmp == '':
        tmp = 'a'
        
    # 6단계
    if len(tmp) >= 16:
        tmp = tmp[:15]
        if tmp[-1] == '.':
            tmp = tmp[:-1]
    
    # 7단계
    if len(tmp) <= 3:
        tmp = tmp + tmp[-1]*(3-len(tmp))
        
    return tmp