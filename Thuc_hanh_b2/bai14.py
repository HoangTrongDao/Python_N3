from datetime import datetime
class Ca_thi:
    def __ini__(self, id_n,ngay,gio,phong):
        self.ma = f"C{id_n:03d}"
        self.ngay=ngay.strip()
        self.gio=gio.strip()
        self.phong=phong.strip()
        self.time_1=datetime.strptime(f"{self.ngay} {self.gio}", "%d/%m/%Y %H:%M")

    def __str__(self):
        return f"{self.ma} {self.ngay} {self.gio} {self.phong}"
def solve():
    with open("CATHI.in","r") as file:
        lines = file.readline().strip()
    if not lines:
        return
    n = int(lines)
    ds = []

    idx =1
    for i in range(1,n+1):
        if idx + 2< len(lines):
            ngay = file.readline().strip()
        
            gio = file.readline().strip()
            phong = file.readline().strip()

            ds.append(Ca_thi(i,ngay,gio,phong))
            idx+=3
    ds.sort(key=lambda x:(x.time_1,x.ma))
    for ca in ds:
        print(ca)
if __name__ == "__main__":
    solve()