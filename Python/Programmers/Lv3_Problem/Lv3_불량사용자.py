from itertools import permutations

def match(per, banned_id):
    for i in range(len(per)):
        if len(per[i]) != len(banned_id[i]):
            return False
        for j in range(len(per[i])):
            if banned_id[i][j] == '*':
                continue
            if per[i][j] != banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    ans = []
    for i in permutations(user_id, len(banned_id)):
        if match(i, banned_id):
            i = set(i)
            if i not in ans:
                ans.append(i)
    
    return len(ans)