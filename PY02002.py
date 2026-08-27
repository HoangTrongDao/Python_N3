import sys
def fibo(n):
    a = 1
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    return a
try:

    t = int(input())
    while t:
        a,b = map(int,input().split())
        for i in range(a,b+1):
            print(fibo(i),end = " ")
        print()   
        t-=1

except EOFError:
    pass