import sys
try:
    t = int(input())
    a = list(map(int,input().split()))
    cnt=0
    for i in range(t-1):
        if a[i]!=a[i+1]:
            cnt+=1
    print(cnt)
except EOFError:
    pass