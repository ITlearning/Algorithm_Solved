def solution(skill, skill_trees):
    board = list(skill)
    cnt = 0
    for i in skill_trees:
        tmp = ""
        for j in i:
            if j in board:
                tmp += j
        if skill.startswith(tmp) == True:
            cnt += 1
    return cnt