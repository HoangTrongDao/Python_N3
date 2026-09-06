import math
def nt(n):
    if n<2:
        return False
    for i in range(2,(int(math.sqrt(n)+1))):
        if n%i==0:
            return False
    return True
t = int(input())
while t:
    n = int(input())
    n = str(n)
    dau = n[:3]
    dau = int(dau)
    cuoi =n[-3:]
    cuoi= int(cuoi)
    if nt(dau) and nt(cuoi):
        print("YES\n")
    else:
        print("NO\n")
    t-=1