n = int(input())
a = list(map(float,input().split()))
mn = min(a)
mx = max(a)
b = []
for x in a:
    if x != mn and x != mx:
        b.append(x)
avg = sum(b) / len(b)
print(f"{avg:.2f}")