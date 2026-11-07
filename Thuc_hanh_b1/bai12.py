
t = int(input())
while t:
    n = input().strip()
    tic = 1
    tong = 0
    co_so_le=False
    for i in range(len(n)):
        x = int(n[i])
        if i%2==0:
            tong+=x
        else:
            if x!=0:
                tic*=x
                co_so_le=True
    if not co_so_le:
        tic=0
    print(tong,tic)
    print()
    t-=1