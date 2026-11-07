import sys
import math
def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
n = int(input())
a = list(map(int,input().split()))
a.sort()
for i in range(n):
    for j in range(i+1,n):
        if math.gcd(a[i],a[j])==1:
            print(a[i],a[j])