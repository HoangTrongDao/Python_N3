import math
def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def dk(n):
    s = str(n)
    for i in range(len(s)):
        vt = i  
        cs = int(s[i])

        if nt(vt) != nt(cs):
            return False

    return True
t = int(input())
for _ in range(t):
    s = input().strip()
    if dk(s):
        print("YES")
    else:
        print("NO")
