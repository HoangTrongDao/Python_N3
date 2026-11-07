import sys
def check(s1,s2):
    return sorted(s1)==sorted(s2)
t = int(input())
for i in range(1,t+1):
    s1=input()
    s2=input()
    if check(s1,s2):
        kq="YES"
    else:
        kq="NO"
    print(f"Test {i}: {kq}")
    