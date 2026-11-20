n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
if n == m:
    for i in range(n):
        print(*a[i])
elif n>m:
    xoa = n - m
    da_x = 0
    for i in range(n):
        if i % 2==0 and da_x<xoa:
            da_x+=1
            continue
        print(*a[i])
elif m>n:
    cot = m-n
    for i in range(n):
        da_x = 0
        for j in range(m):
            if j % 2 == 1 and da_x<cot:
                da_x+=1
                continue
            print(a[i][j],end=" ")
        print()