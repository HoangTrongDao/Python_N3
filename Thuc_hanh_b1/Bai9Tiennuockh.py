import sys
import math
class Kh:
    def __init__(self,id_n,name="",cu=0,moi=0):
        self.ma = f"KH{id_n:02d}"
        self.name=name
        self.cu=cu
        self.moi=moi
    def  nhap(self):
        self.name = input()
        self.cu = int(input())
        self.moi = int(input())
    def tinh_toan(self):
        l = self.moi-self.cu
        if l<=50:
            tg=l*100
            p=0.02
        elif l<=100:
            tg=(50*100)+((l-50)*150)
            p=0.03
        else:
            tg=(50*100)+(50*150)+((l-100)*200)
            p=0.05
        total=tg*(1+p)
        return round(total)
    def kq(self):
        print(f"{self.ma} {self.name} {self.tinh_toan()}")
t = int(input())
ds = []
for i in range(1,t+1):
    moi1=Kh(id_n=i)

    moi1.nhap()
    ds.append(moi1)
ds.sort(key=lambda x:x.tinh_toan(),reverse=True)
for kh in ds:
    kh.kq()

