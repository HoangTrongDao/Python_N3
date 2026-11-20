import math
vitri1 = []
vitri2 = []
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
max_1 = a[0][0]
min_1 = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j]>max_1:
            max_1 = a[i][j]
            vitri1 = [(i,j)]
        elif a[i][j]==max_1:
            vitri1.append((i,j))
for i in range(n):
    for j in range(m):
        if a[i][j]<min_1:
            min_1 = a[i][j]
            vitri2 = [(i,j)]
        elif a[i][j]==min_1:
            vitri2.append((i,j))
x = max_1 - min_1
vitri = []
for i in range(n):
    for j in range(m):
        if a[i][j]==x:
            vitri.append((i,j))
if len(vitri)>0:
    print(x)
    for i,j in vitri:
        print(f"Vi tri [{i}][{j}]")
else:
    print("NOT FOUND")