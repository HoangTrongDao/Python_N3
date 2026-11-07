n = int(input())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
k = int(input())
tog_tren=0
tog_duoi=0
for i in range(n):
    for j in range(n):
        if i<j:
            tog_tren+=a[i][j]
        elif i>j :
            tog_duoi+=a[i][j]
c_l = abs(tog_tren-tog_duoi)
if c_l<=k:
    print("YES")
else:
    print("NO")
print(c_l)
