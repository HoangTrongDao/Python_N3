import sys
import math
def nt(n):
    if n<2:
        return False
    for i in range(2,(int(math.sqrt(n)+1))):
        if n%i==0:
            return False
    return True
def tong(n):
    t = 0
    while n!=0:
        so = n%10
        t +=so
        n//=10
    return t
def chan(n):
    s = str(n)

    for i in range(0,len(s),2):
        so = int(s[i])
        if so %2!=0:
            return False

    return True

def le(n):
    s = str(n)

    for i in range(1,len(s),2):
        so = int(s[i])
        if so %2==0:
            return False

    return True

t = int(input())
while t:
    n = int(input())
    kq = tong(n)
    if nt(kq) and chan(n) and le(n):
        print("YES\n")
    else:
        print("NO\n")
    t-=1