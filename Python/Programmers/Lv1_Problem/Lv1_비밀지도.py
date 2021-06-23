def solution(n, arr1, arr2):
    answer = []
    binary1 = []
    binary2 = []
    tmp1 = ""
    tmp2 = ""
    for x,y in zip(arr1,arr2):
        tmp1 = format(x,'b')
        tmp2 = format(y,'b')
        
        binary1.append([tmp1.zfill(n)])
        binary2.append([tmp2.zfill(n)])
        
    for a,b in zip(binary1, binary2):
        tmp = ""
        for i in range(n):
            if a[0][i] == '0' and b[0][i] == '0':
                tmp += " "
            elif a[0][i] == '1' or b[0][i] == '1':
                tmp += "#"
        answer.append(tmp)
    return answer