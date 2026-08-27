import sys
import math
def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
try:
    n,x = map(int,input().split())
    print(x,end=" ")
    cnt=0
    p = 2
    while cnt<n:
        if nt(p):
            x+=p
            print(x,end=" ")
            cnt+=1
        p+=1

except EOFError:
    pass

