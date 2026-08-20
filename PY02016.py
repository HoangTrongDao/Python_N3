import sys
try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))

        dem = {}
        for x in a:
            dem[x] = dem.get(x,0)+1
        ans=-1
        max_count=0

        for x in dem:
            if dem[x]>max_count:
                max_count = dem[x]
                ans = x
            elif dem[x]==max_count and x<ans:
                ans=x
        if max_count > n // 2:
            print(ans)
        else:
            print("NO")
except EOFError:
    pass