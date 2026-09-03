import sys
try:
    t = int(input())
    for _ in range(t):
        s = input()
        kq = True
        for i in range(len(s)-1):
            if int(s[i])>int(s[i+1]):
                kq=False
                break
        if(kq):
            print("YES\n")
        else:
            print("NO\n")
except  EOFError:
    pass
