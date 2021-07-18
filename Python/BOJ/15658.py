# 연산자 끼워넣기
import sys
input = sys.stdin.readline

mini = 999999999999
maxi = -999999999999

n = int(input())
num = list(map(int,input().split()))
plus, minus, mul, div = map(int,input().split())

def dfs(index, result, plus, minus, mul, div):
    global maxi, mini
    if index == n:
        maxi = max(maxi, result)
        mini = min(mini, result)
        return
    if plus > 0:
        dfs(index+1, result + num[index], plus-1, minus, mul, div)
    if minus > 0:
        dfs(index+1, result - num[index], plus, minus-1, mul, div)
    if mul > 0:
        dfs(index+1, result * num[index], plus, minus, mul-1, div)
    if div > 0:
        dfs(index+1, int(result / num[index]), plus, minus, mul, div-1)

dfs(1, num[0], plus, minus, mul, div)

print(maxi)
print(mini)
