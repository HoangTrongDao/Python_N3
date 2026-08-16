import math
def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)) +1 ):
        if n%i==0:
            return False
    return True
n,m = map(int,input().split())
a = []
for i in range(n):
    hang = list(map(int,input().split()))
    a.append(hang)
for i in range(n):
    for j in range(m):
        if nt(a[i][j]):
            a[i][j]=1
        else:
            a[i][j]=0
for hang in a:
    for value in hang:
        print(value, end = " ")
    print()
