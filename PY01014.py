def lietke(a,k,n):
    kq = ((a+1)+k-1) // k*k
    c = []
    for sum in range(kq,n+1,k):
        b = sum - a
        c.append(b)
    return c

a,k,n = list(map(int,input().split()))
list_kq=lietke(a,k,n)
if list_kq:
    print(*list_kq)
else:
    print(-1)