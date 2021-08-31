from itertools import permutations, product
from itertools import combinations

def binary_search(point, item):
    start = 1
    end = len(item)
    #print(point)
    #print(item)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        #print(item[mid-1][1], point)
        if item[mid-1][1] >= point:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


def cc(copy, i, items, index, tu):
    for k in range(0,4):
        i[k] = '-'
        repl = tuple(i[:4])
        for j in product(repl, repeat=4):
            if j in tu:
                if len(items[j]) != 0:
                    if [index,int(i[4])] not in items[j] :
                        items[j].append([index,int(i[4])])       
                else:
                    if [index,int(i[4])] not in items[j]:
                        items[j].append([index,int(i[4])])          
            i = copy[:]

def solution(info, query):
    answer = []
    player = []
    items = {}
    que = []
    language = ['cpp','java', 'python', '-']
    location = ['frontend','backend', '-']
    year = ['junior','senior', '-']
    food = ['chicken', 'pizza', '-']
    tu = []
    
    for i in product(language, location, year, food):
        #print(i)
        tu.append(i)
        items[i] = []
        
    
    for i in info:
        tmp = i.split()
        player.append(tmp)
    
    for index,i in enumerate(player):
        d = tuple(i[:4])
        copy = i[:]
        items[d].append([index,int(i[4])])
        cc(copy,i,items, index, tu)
        
    
    for i in query:
        qq = i.replace("and", "")
        tmp = qq.split()
        que.append(tmp)
        #print(tmp)
        #que.append(t)
        
    for q in que:
        check = tuple(q[:4])
        items[check].sort(reverse=True,key=lambda x: int(x[1]))
        #print(items[check])
        p = binary_search(int(q[4]), items[check])
        answer.append(p)
        
    
    
    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(info,query))