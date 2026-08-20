import sys
def tic(n):
    tich = 1
    co_so = False
    for i in range(len(n)):
        if i % 2 != 0:
            if int(n[i]) != 0:
                tich *= int(n[i])
                co_so = True
    if co_so == False:
        return 0
    return tich
def tong(n):
    t = 0
    for i in range(len(n)):
        if i%2==0:
            t+=int(n[i])
    return t
try:
    t = int(input())
    for _ in range(t):
        n = input()
        kq1 = tic(n)
        kq2 = tong(n)
        print(kq2,kq1)
    print("\n")
except EOFError:
    pass