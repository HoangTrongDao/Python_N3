import sys
import math
def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n,m = map(int,input().split())
a = []
for i in range(n):
    row = list(map(int,input().split()))
    a.append(row)
b = []
for row in a:
    new_row=[]
    for val in row:
        if nt(val):
            new_row.append(1)
        else:
            new_row.append(0)
    b.append(new_row)
for row in b:
    print(*row)