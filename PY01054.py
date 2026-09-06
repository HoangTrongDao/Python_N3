import sys
def tic(n):
    t = 1
    while n !=0:
        so = n%10
        if so != 0:
            t*=so
        n//=10
    return t
t = int(input())
while t:
    n = int(input())
    print(tic(n))
    t-=1