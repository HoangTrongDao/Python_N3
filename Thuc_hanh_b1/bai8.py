import math
import sys
data = list(map(int,sys.stdin.read().split()))
n = data[0]
a = data[1:n+1]
chan = []
le = []
for c in a:
    if c%2==0:
        chan.append(c)
    else:
        le.append(c)
chan.sort()
le.sort(reverse=True)
i_chan=0
i_le=0
for i in range(n):
    if a[i]%2==0:
        a[i]=chan[i_chan]
        i_chan+=1
    else:
        a[i]=le[i_le]
        i_le+=1
print(*a)