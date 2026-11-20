import math
def tn(n):
    s = str(n)
    return   len(s) >= 2 and s == s[::-1]
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
vitri = []
max_tn = -1
for i in range(n):
    for j in range(m):
        if(tn(a[i][j])):
            if a[i][j]>max_tn:
                max_tn = a[i][j]
                vitri = [(i,j)]
            elif a[i][j]==max_tn:
                vitri.append((i,j))
if max_tn!=-1:
    print(max_tn)
    for i, j in vitri:
            print(f"Vi tri [{i}][{j}]")
else:
    print("NOT FOUND")