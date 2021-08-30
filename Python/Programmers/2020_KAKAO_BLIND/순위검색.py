from itertools import permutations
from itertools import combinations
def solution(info, query):
    answer = []
    player = []
    que = []
    items = {
        'cpp': 
        {
            'backend': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            },
            'frontend': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            },

            '-': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                '-':
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            }
        },
        
        'java':
        {
            'backend': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            },
            'frontend': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            },

            '-': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                '-':
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            }
        },
        
        'python':
        {
            'backend': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            },
            'frontend': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            },

            '-': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                '-':
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            }
        },

        '-': 
        {
            'backend': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            },
            'frontend': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            },

            '-': 
            {
                'junior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                'senior': 
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                },
                '-':
                {
                    'pizza': [],
                    'chicken': [],
                    '-': []
                }
            }
        }

    }
    
    
    for i in info:
        tmp = i.split()
        player.append(tmp)
    
    for p in player:
        language = ['cpp','java', 'python', '-']
        location = ['frontend','backend', '-']
        year = ['junior','seinor', '-']
        food = ['chicken', 'pizza', '-']

        items[p[0]][p[1]][p[2]][p[3]].append(p[4])
        p[0] = '-'
        tmp = list(permutations(p[:4],4))
        #print(tmp)
        for i in tmp:
            #print(i)
            if (i[0] in language) and (i[1] in location) and (i[2] in year) and (i[3] in food) :
                items[i[0]][i[1]][i[2]][i[3]].append(p[4])   
        
        p[1] = '-'
        tmp = list(permutations(p[:4],4))
        #print(tmp)
        for i in tmp:
            #print(i)
            if (i[0] in language) and (i[1] in location) and (i[2] in year) and (i[3] in food) :
                items[i[0]][i[1]][i[2]][i[3]].append(p[4])       
        p[2] = '-'
        tmp = list(permutations(p[:4],4))
        #print(tmp)
        for i in tmp:
            #print(i)
            if (i[0] in language) and (i[1] in location) and (i[2] in year) and (i[3] in food) :
                items[i[0]][i[1]][i[2]][i[3]].append(p[4]) 
        p[3] = '-'
        tmp = list(permutations(p[:4],4))
        #print(tmp)
        for i in tmp:
            #print(i)
            if (i[0] in language) and (i[1] in location) and (i[2] in year) and (i[3] in food) :
                items[i[0]][i[1]][i[2]][i[3]].append(p[4]) 

    #print(items)
    
    for q in query:
        qq = q.replace("and", "")
        tmp = qq.split()
        que.append(tmp)
    cnt = 1
    for i in que:
        print(i[0],i[1],i[2],i[3])
        print(items[i[0]][i[1]][i[2]][i[3]])
        print()
        
            
    
    return answer

solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])