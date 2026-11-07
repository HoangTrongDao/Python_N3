from itertools import combinations
n,k = map(int,input().split())
a = input().split()
a = sorted(set(a))
for x in combinations(a,k):
    print(*x)