import sys
try:
    def tn(s):
        return s == s[::-1]
    def so_chan(s):
        return all(int(digit)%2==0 for digit in s)
    def dem_chan(n):
        s = str(n)
        return len(s)%2==0
    
    t = int(input())
    for _ in range(t):
        kq=[]
        n = int(input())
        for i in range(22,n):
            s = str(i)
            if tn(s)  and so_chan(s) and dem_chan(s):
                kq.append(s)
        print(" ".join(kq))
except EOFError:
    pass