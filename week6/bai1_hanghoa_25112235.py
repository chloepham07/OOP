from abc import ABC, abstractmethod
class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f'gia {gia} khong hop le')

class HangHoa(ABC):
    def __init__(self, ma, ten, nhasx, gia):
        self.__ma, self.__ten, self.__nhasx = ma , ten , nhasx
        self.gia = gia

    @property
    def ma_hang(self): return self.__ma

    @property
    def ten_hang(self): return self.__ten
    
    @property
    def gia(self): return self.__gia

    @gia.setter
    def gia(self, value : int):
        if value < 0 : raise GiaKhongHopLe(value)
        self.__gia = value

    @abstractmethod
    def loai_hang(self): pass
    def inTTin(self):
        return (f"[{self.loai_hang()}] {self.__ma} | {self.__ten} | {self.__gia:,.0f}đ")

    def __str__(self): return self.inTTin()
    def __eq__(self,other): return self.__ma == other.__ma
    def __lt__(self,other): return self.__gia < other.__gia
    def __hash__(self): return hash(self.__ma)

class HangDienMay(HangHoa):
    def __init__(self, ma, ten , nhasx , gia , baohanh , dienap , congsuat):
        super().__init__(ma, ten , nhasx , gia)
        self.__baohanh, self.__dienap, self.__congsuat = baohanh , dienap , congsuat

    def loai_hang(self): 
        return "Dien may"

    def inTTin(self): 
         return (f"{super().inTTin()} | Bao hanh : {self.__baohanh}thang | Dien ap : {self.__dienap}V | Cong suat : {self.__congsuat}W")

class HangSanhSu(HangHoa):
    def __init__(self, ma, ten , nhasx , gia , loainguyenlieu):
        super().__init__(ma, ten , nhasx , gia)
        self.__loainguyenlieu = loainguyenlieu

    def loai_hang(self):
        return  "Hang sanh su"
    
    def inTTin(self): 
         return (f"{super().inTTin()} | Loai nguyen lieu :{self.__loainguyenlieu}")
    
class HangThucPham(HangHoa):
    def __init__(self, ma, ten , nhasx , gia , nsx , hsd ):
        super().__init__(ma, ten , nhasx , gia)
        self.nsx = nsx
        self.hsd = hsd

    def loai_hang(self):
        return "Thuc pham"
    
    def inTTin(self):
        return (f"{super().inTTin()} | ngay san xuat: {self.nsx} | han su dung: {self.hsd}")
    
# Context Manager: luu danh sach vao file 
def luu_file(ds, ten_file="hanghoa.txt"):
    """Ghi toan bo danh sach hang hoa ra file van ban."""
    with open(ten_file, "w", encoding="utf-8") as f:
        for sp in sorted(ds):           # __lt__ sap xep theo gia
            f.write(f"{sp}\n")
    print(f"Da luu {len(ds)} san pham vao '{ten_file}'")


# Context Manager: doc danh sach tu file 
def doc_file(ten_file="hanghoa.txt"):
    """Doc va in noi dung file hang hoa."""
    print(f"\n--- Noi dung file '{ten_file}' ---")
    with open(ten_file, "r", encoding="utf-8") as f:
        for dong in f:
            print(dong)


# Demo 
ds = [
    HangDienMay('DM001', 'Tu lanh', 'panasony', 1000, 12, 220, 150),
    HangSanhSu ('SS002', 'Lo hoa',  'ABC',      100, 'gom'),
    HangThucPham('TP003', 'Sua',    'Vinamilk',  10, '06/12/2025', '06/12/2026'),
    HangDienMay('DM004', 'May giat','LG',        800, 24, 220, 500),
]

# 1. __str__ 
for sp in ds:
    print(sp)

# 2. __lt__ + sorted : sap xep theo gia
for sp in sorted(ds):
    print(f"  {sp.ten_hang}: {sp.gia:,}d")

# 3. __eq__ : so sanh theo ma hang
print("\n __eq__: so sanh ")
a = HangSanhSu('SS002', 'ban sao', 'xyz', 999, 'su')
print(f"a == ds[1] (cung ma SS002)? {a == ds[1]}")   # True
print(f"a == ds[0] (khac ma)?       {a == ds[0]}")   # False

# 4. __hash__ + set : loai trung
print("\n __hash__: set() loai trung ")
ds_trung = ds + [HangSanhSu('SS002', 'trung lap', 'abc', 50, 'su')]
print(f"List: {len(ds_trung)} phan tu")
print(f"Set : {len(set(ds_trung))} phan tu (SS002 bi loai)")

# 5. Context Manager : luu va doc file
luu_file(ds)
doc_file()
