import math
def nt(n):
    if n<2:
        return False
    for i in range(2,(int(math.sqrt(n)+1))):
        if n%i==0:
            return False
    return True
n = int(input())
a = list(map(int,input().split()))
d = 0
tx = {}
for i in a:
    if i in tx:
        tx[i]+=1
    else:
        tx[i]=1
for i in tx:
    if nt(i):
        print(f"{i} {tx[i]}")