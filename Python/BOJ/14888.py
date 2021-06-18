# 연산자 끼워넣기
# 백트래킹 문제
import sys
input = sys.stdin.readline
def dfs(cnt, result, pl,mi, mul, div):
    global max_result
    global min_result
    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if pl:
        dfs(cnt+1, result+s[cnt], pl-1, mi, mul, div)
    if mi:
        dfs(cnt+1, result-s[cnt], pl, mi-1, mul, div)
    if mul:
        dfs(cnt+1, result*s[cnt], pl, mi, mul-1, div)
    if div:
        dfs(cnt+1, -(-result//s[cnt]) if result < 0 else result // s[cnt], pl, mi,mul, div-1)

n = int(input())
s = list(map(int,input().split()))
op = list(map(int,input().split()))
max_result = -1000000001
min_result = 1000000001
dfs(1,s[0], op[0],op[1],op[2],op[3])
print(max_result)
print(min_result)