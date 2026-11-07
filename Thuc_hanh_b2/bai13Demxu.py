n = int(input())

a = []
for _ in range(n):
    a.append(input().strip())

tog=0
for i in range(n):
    k = a[i].count('C')
    if k>=2:
        tog+=(k*(k-1))//2

for j in range(n):
    k=0
    for i in range(n):
        if a[i][j]=='C':
            k+=1
    if(k>=2):
            tog+=(k*(k-1))//2
print(tog)