import math
def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)    ):
        if n%i==0:
            return False
    return True
n = int(input())
a = list(map(int,input().split()))
b = []
c = []
for i in a:
    if nt(i):
        b.append(i)
    else:
        c.append(i)
dem = 0
for i in c:
    trai = i-1
    phai = i+1
    buoc = 1
    while(True):
        if (trai>=2 and nt(trai)) or nt(phai):
            if buoc>dem:
                dem = buoc
            break
        trai-=1
        phai+=1
        buoc+=1
print(dem)
