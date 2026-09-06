import sys
import math
def d_n(n):
    return n[::-1]
try:
    t = int(input())
    while t:
        n = input()
        kq = d_n(n)
        if (math.gcd(int(n),int(kq)))==1:
            print("YES\n")
        else:
            print("NO\n")
        t-=1
except EOFError:
    pass
