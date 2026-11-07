import math
def nt(n):
    if n<2:
        return False
    for i in range(2,(int(math.sqrt(n)))+1):
        if n%i==0:
            return False
    return True
t = int(input())
while t:
    k = 0
    n = int(input())
    for i in range(n):
        if (math.gcd(i,n))==1:
            k+=1
    if nt(k):
        print("YES")
    else:
        print("NO")
    t-=1