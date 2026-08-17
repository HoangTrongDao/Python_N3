import sys
try:
    t = int(input())
    while t:
        n = input()
        if n.endswith("86"):
            print("YES\n")
        else:
            print("NO\n")
            
except EOFError:
    pass