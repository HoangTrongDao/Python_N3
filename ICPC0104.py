from re import *
t = int(input())
while t > 0:
    a = input()
    li = findall(r"\d+", a)
    if li:
        li_ints = [int(x) for x in li]
        print(min(li_ints))
    t -= 1
