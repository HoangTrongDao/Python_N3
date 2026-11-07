import sys
def dk1(n):
    s = str(n)
    return len(s) % 2==1
def dk2(n):
    s = str(n)
    return s[0]!=s[1]
def dk3(n):
    s = str(n)
    return all(s[i] == s[0] for i in range(2, len(s), 2))
n = int(input())
for _ in range(n):
    s = input()
    if dk1(s) and dk2(s) and dk3(s):
        print("YES\n")
    else:
        print("NO\n")
