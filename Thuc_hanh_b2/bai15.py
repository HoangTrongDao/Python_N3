with open('DATA1.in','r') as f1:
    tu1= set(f1.read().lower().split())
with open('DATA2.in','r') as f2:
    tu2= set(f2.read().lower().split())
kq1 = sorted(list(tu1-tu2))
kq2 = sorted(list(tu2-tu1))
print(*kq1)
print(*kq2)