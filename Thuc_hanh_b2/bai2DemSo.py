from collections import Counter
s = input().strip()
k = int(input())

a = []
i = 0
while i<len(s)-1:
    num = int(s[i:i+2])
    a.append(num)
    i+=2
dem = Counter(a)

kq=[]
for num, count in dem.items():
    if count>=k:
        kq.append((num,count))

kq.sort(key=lambda x:x[0])

if len(kq)==0:
    print("NOT FOUND")
else:
    for num, count in kq:
        print(f"{num} {count}")