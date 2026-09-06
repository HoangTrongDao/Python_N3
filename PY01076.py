import math
t = int(input())
while t:
    a = int(input())
    b = int(input())
    kq = math.gcd(a,b)
    print(kq)
    t-=1