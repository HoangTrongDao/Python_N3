import math
def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
t = int(input())
a = list(map(int,input().split()))
tan_xuat = []
for x in a:
    if nt(x) and x not in tan_xuat:
        dem = a.count(x)
        print(x,dem)
        tan_xuat.append(x)