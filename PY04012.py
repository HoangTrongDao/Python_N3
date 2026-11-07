class Lop:
    def __init__(self, id,ten,lop1):
        self.id = id
        self.ten=ten
        self.lop1=lop1
        self.diem = 10
    def tinh_diem(self, diem_danh):
        for c in diem_danh:
            if c == 'm':
                self.diem -= 1
            elif c == 'v':
                self.diem -= 2

        if self.diem < 0:
            self.diem = 0
    def in_ra(self):
        print(f"{self.id} {self.ten} {self.lop1} {self.diem}",end="")
        if self.diem == 0:
            print(" KDDK")
        else:
            print()

n = int(input())
ds = []
for i in range(n):
    id = input()
    ten = input()
    lop = input()

    sv = Lop(id, ten, lop)
    ds.append(sv)
for i in range(n):
    data = input().split()

    id = data[0]
    diem_danh = data[1]
    for sv in ds:
        if sv.id == id:
            sv.tinh_diem(diem_danh)
            break
for sv in ds:
    sv.in_ra()