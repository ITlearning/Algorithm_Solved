# 접두사 찾기
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

strings = [input().strip() for _ in range(n)]
#print(strings)
cnt = 0
for _ in range(m):
    pattern = input().rstrip()
    for s in strings:
        if s.startswith(pattern):
            cnt += 1
            break

print(cnt)
