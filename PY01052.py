import sys
import math
def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
def tong(n):
    s = 0
    while n!=0:
        ss = n%10
        s +=ss
        n//=10
    return s
try:
    t = int(input())
    while t:
        n = int(input())
        kq = tong(n)
        if(nt(kq)):
            print("YES\n")
        else:
            print("NO\n")
        t-=1
except EOFError:
    pass