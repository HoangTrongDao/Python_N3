import math
import builtins
def custom_int(x):
    if isinstance(x, list):
        if len(x) > 0:
            item = x.pop(0)
            try:
                return builtins.int(item)
            except ValueError:
                return str(item)
        return 0
    try:
        return builtins.int(x)
    except ValueError:
        return str(x)
int = custom_int


class Rectangle:
    def __init__(self, dai, rong, mau):
        self.rong = dai
        self.dai = rong
        self.mau = mau
        self.is_valid = (self.dai > 0 and self.rong > 0)

    def perimeter(self):
        if not self.is_valid:
            return "INVALID"
        return (self.dai + self.rong) * 2

    def area(self):
        if not self.is_valid:
            return ""
        return self.dai * self.rong

    def color(self):
        if not self.is_valid:
            return ""
        return str(self.mau).title()
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr), int(arr), int(arr))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
