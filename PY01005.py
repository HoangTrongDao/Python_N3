def cntB(n):
    cnt4=0
    while n!=0:
        so = n%10
        if so==4:
            cnt4+=1
        n//=10
    return cnt4
def cntb(n):
    cnt7=0
    while n!=0:
            so = n%10
            if so==7:
                cnt7+=1
            n//=10
    return cnt7

n = int(input())
kq1 = cntB(n)
kq2 = cntb(n)
if kq1+kq2==4:
     print("YES\n")
elif kq1+kq2==7:
     print("YES\n")
else:
     print("NO\n")