import sys

def tong(n):
    t = 1
    s = int(n)
    if s == 0: 
        return 0 
    while (s != 0):
        so = s % 10
        t *= so
        s //= 10
    return t
input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    idx = 1
    
    while (t > 0):  
     
        n = int(input_data[idx])
        idx += 1
        a = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        
        b = []
        for i in a:
            kq = tong(i)
            b.append((kq, i))
        
        b.sort()
        for i in b:
            print(i[1], end=" ")
        print() 
        t -= 1
