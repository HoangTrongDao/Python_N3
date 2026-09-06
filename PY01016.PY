import sys
try:
    t = int(input())
    while t:
        s = input()
        kq = ""
        i = 0
        while i<len(s):
            char = s[i]
            i+=1
            num=""
            while i<len(s) and s[i].isdigit():
                num+=s[i]
                i+=1
            if num:
                kq += char*int(num)
            else:
                kq+=char
        print(kq)
        t-=1
except EOFError:
    pass