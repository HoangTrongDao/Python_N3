import math
n = int(input())
a = list(map(int, input().split()))
dem = -1
min_st = float("inf")
for i in a:
    d = 0
    for x in a:
        d +=abs(x-i)
    if d<min_st:
            min_st = d
            dem = i
print(min_st,dem)