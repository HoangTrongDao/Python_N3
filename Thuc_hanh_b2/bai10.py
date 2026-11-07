import sys
import math
class Dn:
    def __init__(self,id_n,name="",lt=0.0,th=0.0):
        self.ma = f"TS{id_n:02d}"
        self.name = name
        self.lt=lt
        self.th=th
    def ch(self,diem_str):
            d = float(diem_str.strip())
            if d>10:
                d/=10
            return d
    def nhap(self):
        self.name = input().strip()
        self.lt = self.ch(input())
        self.th = self.ch(input())
   
    def tb(self):
        kq = round((self.lt+self.th)/2,2)
        return kq
    def xl(self):
        kq = self.tb()
        if kq<5:
            return "TRUOT"
        elif kq>=5 and kq<8:
            return "CAN NHAC"
        elif  kq>=8 and kq<=9.5:
            return "DAT"
        else:
            return "XUAT SAC"
    def out_p(self):
        print(f"{self.ma} {self.name} {self.tb():.2f} {self.xl()}")
t = int(input())
ds = []
for i in range(1,t+1):
    kh1 = Dn(id_n=i)
    kh1.nhap()
    ds.append(kh1)
ds.sort(key=lambda x:x.tb(),reverse=True)
for kh in ds:
    kh.out_p()