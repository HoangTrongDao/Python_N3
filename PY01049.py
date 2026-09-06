import sys
import math
def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n% i ==0:
            return False
    return True
def dk(n):
    s = str(n)
    #dk2
    if not nt(len(s)):
        return False
    #dk1 
    nt1 = 0
    nt2 = 0
    for c in s:
        if c in "2357":
            nt1+=1
        else:
            nt2+=1
    return nt1>nt2

try:
    t = int(input())
    while t:
        n = int(input())
        if dk(n):
            print("YES\n")
        else:
            print("NO\n")
        t-=1
except EOFError:
    pass