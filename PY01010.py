t = int(input())

while t:
    n = input()

    kq1 = n[0]+n[1]
    kq2 = n[-2]+n[-1]
  
    if(int(kq1) == int(kq2)):
        print("YES\n")
    else:
        print("NO\n")
    t-=1
