import math
def nt(n):
    if n<2:
        return False
    for i in range(2,(int(math.sqrt(n)+1))):
        if n%i==0:
            return False
    return True    
n,m = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]
max_tn = -1
vi_tri = []  
for i in range(n):
    for j in range(m):
        if nt(a[i][j]):
            if a[i][j]>max_tn:
                max_tn = a[i][j]
                vi_tri = [(i,j)]
            elif a[i][j]==max_tn:
                vi_tri.append((i,j))
                
if max_tn !=-1:
    print(max_tn)
    for i, j in vi_tri:
        print(f"Vi tri [{i}][{j}]")
else:
    print("NOT FOUND")