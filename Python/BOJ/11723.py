# 집합
import sys
input = sys.stdin.readline
M = int(input())
S = []

def add(x):
    if x not in S:
        S.append(x)

def remove(x):
    if x in S:
        S.pop(S.index(x))

def check(x):
    if x in S:
        return 1
    else:
        return 0

def toggle(x):
    if x in S:
        S.pop(S.index(x))
    else:
        S.append(x)

def all():
    global S
    tmp = []
    for i in range(1,21):
        tmp.append(i)
    S = tmp[:]

def empty():
    global S
    S = []

for _ in range(M):
    text = input().split()
    if text[0] == 'add':
        add(int(text[1]))
    elif text[0] == 'check':
        print(check(int(text[1])))
    elif text[0] == 'remove':
        remove(int(text[1]))
    elif text[0] == 'toggle':
        toggle(int(text[1]))
    elif text[0] == 'all':
        all()
    elif text[0] == 'empty':
        empty()