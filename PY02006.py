import sys
try:
    t = int(input())
    while t:
        n = int(input())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        a.sort()
        b.sort()
        ok = True
        for i in range(n):
            if a[i]>b[i]:
                ok = False
                break
        if(ok):
            print("YES\n")
        else:
            print("NO\n")
        t-=1

except EOFError:
    pass