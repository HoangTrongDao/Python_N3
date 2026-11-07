import math
class Lop:
    def __init__(self,ma,ten,diem):
        self.ma=ma
        self.ten=ten
        self.diem=diem
        self.dtb=0
        self.kq=""
    def tong(self):
        tong=self.diem[0]*2+self.diem[1]*2
        for i in range(2,10):
            tong+=self.diem[i]
        self.dtb=tong/12+ 1e-9  
    def xl1(self):
        if self.dtb >= 9:
            self.xl = "XUAT SAC"
        elif self.dtb >= 8:
            self.xl = "GIOI"
        elif self.dtb >= 7:
            self.xl= "KHA"
        elif self.dtb >= 5:
            self.xl = "TB"
        else:
            self.xl = "YEU"
    def in_ra(self):
        print(f"{self.ma} {self.ten} {self.dtb:.1f} {self.xl}")

n = int(input())
ds = []

for i in range(n):
    ten = input()
    diem = list(map(float,input().split()))

    ma = f"HS{i+1:02d}"

    hs = Lop(ma,ten,diem)
    hs.tong()
    hs.xl1()
    ds.append(hs)

ds.sort(key=lambda hs:(-hs.dtb,hs.ma))

for hs in ds:
        hs.in_ra()