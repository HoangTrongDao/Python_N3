import math
def chia(n):
    buoc = 0
    while buoc<1001:
        if n%7==0:
            return n
    
        kq = int(str(n)[::-1])
        n = n+kq
        buoc+=1
    return -1

t = int(input())
while t:
    n= int(input())
    print(chia(n))
    t-=1