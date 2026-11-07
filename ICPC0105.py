from re import *
t = int(input())
while(t>0):
    a = input()
    li = findall(r'\d+',a)
    if li:
        li_nit = [int(x) for x in li]
        print(max(li_nit))
    t-=1