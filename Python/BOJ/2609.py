import math
n,m = map(int,input().split())

def lcm(x,y):
    return x * y // math.gcd(x,y)

print(math.gcd(n,m))
print(lcm(n,m))