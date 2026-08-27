t = int(input())

for _ in range(t):
    n = int(input())
    d = {}

    for _ in range(n):
        x = int(input())
        d[x] = d.get(x, 0) + 1

    max_count = max(d.values())

    ans = min(x for x in d if d[x] == max_count)

    print(ans)  