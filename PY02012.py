import sys
try:
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    a = data[1:n+1]
    chan = []
    le = []
    for x in a:
        if x%2==0:
            chan.append(x)
        else:
            le.append(x)
    chan.sort()
    le.sort(reverse=True)
    i = 0
    j = 0
    for k in range(n):
        if a[k] % 2 == 0:
            a[k] = chan[i]
            i += 1
        else:
            a[k] = le[j]
            j += 1
    print(*a)
except EOFError:
    pass
