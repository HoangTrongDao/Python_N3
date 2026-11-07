t = int(input())
while t:
    n = input().strip()
    tic = 1
    tong = 0
    for i in range(len(n)):
        x = int(n[i])
        if i % 2==0:
            if x!=0:
                tic*=x
        else:
            tong+=x
    print(tic,tong)
    print()
    t-=1
            