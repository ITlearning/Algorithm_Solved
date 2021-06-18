# 지능형 기차
import sys
input = sys.stdin.readline
station_number = 10
max_total = 0
total = 0
while station_number != 0:
    go, out = map(int,input().split())
    total -= go
    total += out
    max_total = max(max_total, total)
    station_number -= 1
print(max_total)