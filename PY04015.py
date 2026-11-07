class Hoa_don:
    def __init__(self, ma, ten, cu, moi):
        self.ma = ma
        self.ten = ten
        self.cu = cu
        self.moi = moi
        self.tong_tien = 0

    def tinh_gia(self):
        so_nuoc = self.moi - self.cu

        if so_nuoc <= 50:
            tien = so_nuoc * 100
            phu_phi = 2

        elif so_nuoc <= 100:
            tien = 50 * 100 + (so_nuoc - 50) * 150
            phu_phi = 3

        else:
            tien = 50 * 100 + 50 * 150 + (so_nuoc - 100) * 200
            phu_phi = 5

        self.tong_tien = tien + tien * phu_phi / 100

    def in_ra(self):
        print(f"{self.ma} {self.ten} {self.tong_tien:.0f}")


n = int(input())
ds = []

for i in range(n):
    ten = input()
    cu = int(input())
    moi = int(input())

    ma = f"KH{i + 1:02d}"

    hd = Hoa_don(ma, ten, cu, moi)
    hd.tinh_gia()
    ds.append(hd)

ds.sort(key=lambda hd: -hd.tong_tien)

for hd in ds:
    hd.in_ra()