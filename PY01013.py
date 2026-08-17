import math
def nt(n):
    if n<2:
        return False
    for i in range(2    ,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def ucln(a,b):
    while(b!=0):
        a,b=b,a%b
    return a
def tong(n):
    sum = 0
    while(n!=0):
        so = n%10
        sum+=so
        n//=10
    return sum
try:
    t = int(input())
    for _ in range(t):
        a,b = map(int,input().split())
        kq = ucln(a,b)
        tong_so = tong(kq)
        if(nt(tong_so)):
            print("YES\n")
        else:
            print("NO\n")

except EOFError:
    pass
