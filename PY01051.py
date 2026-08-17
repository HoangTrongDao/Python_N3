import sys
# 1. Hàm kiểm tra số thuận nghịch
def tn(a):
    s = str(a)
    # Điều kiện 1: Số chữ số phải lớn hơn 1
    # Điều kiện 2: Chuỗi đảo ngược phải bằng chính nó
    return len(s) > 1 and s == s[::-1]
def tong(s_num):
    tong_so = 0
    for c in s_num:
        tong_so += int(c)
    return tong_so
try:
    t = int(input())
    for _ in range(t):
        n = input().strip()
        kq = tong(n)
        if(tn(kq)):
            print("YES\n")
        else:
            print("NO\n")
except EOFError:
    pass