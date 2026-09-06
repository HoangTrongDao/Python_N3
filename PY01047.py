import math
def nt(n):
    if n<2:
        return False
    for i in range(2,(int(math.sqrt(n)+1))):
        if n%i == 0:
            return False
    return True
t = int(input())
while t:
    n = int(input())
    n = str(n)
    kq = n[-4:]
    kq = int(kq)
    if nt(kq):
        print("YES\n")
    else:
        print("NO\n")
    t-=1