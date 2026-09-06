import sys
import math
class Thi_sinh:
    def __init__(self,ten,date,t,l,h):
        self.ten =  str(ten)
        self.date = date
        self.t=t
        self.l=l
        self.h=h
    def tong(self):
        return self.t + self.l +self.h

    def __str__(self):
            return "{} {} {:.1f}".format(self.ten, self.date, self.tong())

if __name__ == '__main__':

    ten = input().strip()
    date = input().strip()
    t = float(input())
    l = float(input())
    h = float(input())
    
    ts = Thi_sinh(ten, date, t, l, h)
    
    print(ts)
        