# 숫자 카드 2
import sys
input = sys.stdin.readline

_ = int(input())
N = sorted(map(int,input().split()))
_ = int(input())
M = map(int,input().split())

def binary(n, board, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if n == board[mid]:
        return board[start:end+1].count(n)
    elif n < board[mid]:
        return binary(n, board, start, mid-1)
    else:
        return binary(n, board, mid+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N)-1
    if n not in n_dic:
        n_dic[n] = binary(n,N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M))