# 캐슬 디펜스
from itertools import combinations
from collections import deque
import copy
n,m,d = map(int,input().split())

board = []

def make_one_array():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                one_array.append([i,j])


