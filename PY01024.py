def tong(n):
    sum = 0
    while n!=0:
        s = n%10
        sum +=s
        n//=10
    return sum
def k_c(n):
    a = str(n)
    for i in range(1, len(a)):
        if abs(int(a[i])-int(a[i-1]))!=2:
            return False
    return True
try:
    t = int(input())
    while t:
        n = int(input())
        kq = tong(n)
        if kq%10==0 and k_c(n):
            print("YES\n")
        else:
            print("NO\n")
       
        t-=1
except EOFError:
    pass