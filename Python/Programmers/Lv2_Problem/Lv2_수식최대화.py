def calc(pro, n, expression):
    if n == 2:
        return str(eval(expression))
    if pro[n] == '*':
        res = eval('*'.join([calc(pro,n+1,e) for e in expression.split('*')]))
    if pro[n] == '+':
        res = eval('+'.join([calc(pro,n+1,e) for e in expression.split('+')]))
    if pro[n] == '-':
        res = eval('-'.join([calc(pro,n+1,e) for e in expression.split('-')]))
    return str(res)



def solution(expression):
    answer = 0
    pros = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]
    
    for pro in pros:
        res = int(calc(pro, 0 ,expression))
        answer = max(answer, abs(res))
    return answer