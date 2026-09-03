import sys
try:
    s1 = input()
    s2 = input()
    p = int(input())
    kq = s1[:p-1]+s2+s1[p-1:]
    print(kq)
except EOFError:
    pass