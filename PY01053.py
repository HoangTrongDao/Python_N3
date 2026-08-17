import sys
try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        if(n%3==0):
            print("YES\n")
        else:
            print("NO\n")
except EOFError:
    pass