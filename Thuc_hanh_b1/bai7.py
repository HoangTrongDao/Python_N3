import sys
n = int(input())
dem={}
thu_tu=[]
chu_de = None
for _ in range(n):
    s = sys.stdin.readline().strip()
    if s=="":
        chu_de=None
        continue
    if chu_de is None:
        chu_de=s
        if chu_de not in dem:
            dem[chu_de]=0
            thu_tu.append(chu_de)
    else:
        if s=="Study":
            chu_de=s
            if chu_de not in dem:
                dem[chu_de]=0
                thu_tu.append(chu_de)
        else:
            dem[chu_de]+=1
for x in thu_tu:
    print(f"{x}: {dem[x]}")