from math import gcd

class MauSoBangKhong(Exception):
    def __init__(self):
        super().__init__("Mau so khong duoc bang 0")

class PhanSo:
    def __init__(self, tu, mau):
        self.tu  = tu
        self.mau = mau   

    @property
    def tu(self): return self.__tu

    @tu.setter
    def tu(self, value): self.__tu = value

    @property
    def mau(self): return self.__mau

    @mau.setter
    def mau(self, value):
        if value == 0:
            raise MauSoBangKhong()
        self.__mau = value

    def is_toi_gian(self):
        return gcd(abs(self.__tu), abs(self.__mau)) == 1

    def toi_gian(self):
        g = gcd(abs(self.__tu), abs(self.__mau))
        tu_moi  = self.__tu  // g   # chia lay phan nguyen
        mau_moi = self.__mau // g
        if mau_moi < 0:
            tu_moi, mau_moi = -tu_moi, -mau_moi
        return PhanSo(tu_moi, mau_moi)

    def __add__(self, other):     # phep cong
        return PhanSo(
            self.__tu * other.__mau + other.__tu * self.__mau,
            self.__mau * other.__mau
        ).toi_gian()

    def __sub__(self, other):     # phep tru
        return PhanSo(
            self.__tu * other.__mau - other.__tu * self.__mau,
            self.__mau * other.__mau
        ).toi_gian()

    def __mul__(self, other):     # phep nhan
        return PhanSo(
            self.__tu * other.__tu,
            self.__mau * other.__mau
        ).toi_gian()

    def __truediv__(self, other):  # phep chia
        return PhanSo(
            self.__tu * other.__mau,
            self.__mau * other.__tu
        ).toi_gian()

    def __eq__(self, other):
        a = self.toi_gian()
        b = other.toi_gian()
        return a.__tu == b.__tu and a.__mau == b.__mau

    def __lt__(self, other):
        return self.__tu * other.__mau < other.__tu * self.__mau

    def __gt__(self, other):
        return self.__tu * other.__mau > other.__tu * self.__mau

    def __str__(self):
        ps = self.toi_gian()
        if ps.__mau == 1:
            return str(ps.__tu)             # so nguyen thi in nguyen
        return f"{ps.__tu}/{ps.__mau}"

    def __repr__(self):
        return f"PhanSo({self.__tu}, {self.__mau})"

    def __hash__(self):
        ps = self.toi_gian()                # 2/4 va 1/2 cung hash
        return hash((ps.__tu, ps.__mau))


def nhap_phan_so():
    print("Nhap phan so: ")
    raw = input()
    if '/' in raw:
        tu, mau = map(int, raw.split('/'))
    else:
        tu, mau = int(raw), 1
    return PhanSo(tu, mau)


ds = []
n = int(input("Nhap so luong phan so: "))

for i in range(n):
    print(f"Phan so thu {i+1}")
    try:
        ds.append(nhap_phan_so())
    except MauSoBangKhong as e:
        print(f"Loi: {e} — bo qua")

print("\n 1.Toi gian")
for ps in ds:
    print(f"  {repr(ps)} toi gian la {ps}")

print("\n 2.Sap xep tang dan")
for ps in sorted(ds):
    print(f"  {ps}")

print("\n 3.Phep tinh co ban (phan so dau + cuoi)")
if len(ds) >= 2:
    a, b = ds[0], ds[-1]
    print(f"  {a} + {b} = {a + b}")
    print(f"  {a} - {b} = {a - b}")
    print(f"  {a} * {b} = {a * b}")
    print(f"  {a} / {b} = {a / b}")

print("\n 4.Set loai trung")
print(f"  Truoc: {[repr(p) for p in ds]}")
print(f"  Sau  : {[str(p) for p in set(ds)]}")