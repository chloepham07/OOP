from abc import ABC, abstractmethod

class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        super().__init__(f"Tuoi {tuoi} khong hop le (phai tu 18 den 65)")

class BacKhongHopLe(Exception):
    def __init__(self, bac):
        super().__init__(f"Bac {bac} khong hop le (phai tu 1 den 10)")

class CanBo(ABC):
    def __init__(self, ten, tuoi, gioitinh, diachi):
        self.ten     = ten
        self.tuoi    = tuoi        
        self.gioitinh = gioitinh
        self.diachi  = diachi

    @property
    def tuoi(self): return self.__tuoi

    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(value)
        self.__tuoi = value

    @abstractmethod
    def mo_ta(self): pass          

    def __str__(self):
        return (f"[{self.mo_ta()}] {self.ten} | {self.tuoi} tuoi | {self.gioitinh} | {self.diachi}")

    def __eq__(self, other):
        return self.ten.lower() == other.ten.lower() and self.tuoi == other.tuoi

    def __lt__(self, other):
        return self.ten.lower() < other.ten.lower()  #sap xep theo ten ABC

    def __hash__(self):
        return hash((self.ten.lower(), self.tuoi))

class CongNhan(CanBo):
    def __init__(self, ten, tuoi, gioitinh, diachi, bac):
        super().__init__(ten, tuoi, gioitinh, diachi)
        self.bac = bac             

    @property
    def bac(self): return self.__bac

    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(value)
        self.__bac = value

    def mo_ta(self):              
        return f"Cong nhan | Bac: {self.__bac}"


class KySu(CanBo):
    def __init__(self, ten, tuoi, gioitinh, diachi, nganh):
        super().__init__(ten, tuoi, gioitinh, diachi)
        self.__nganh = nganh

    def mo_ta(self):
        return f"Ky su | Nganh: {self.__nganh}"


class NhanVien(CanBo):
    def __init__(self, ten, tuoi, gioitinh, diachi, congviec):
        super().__init__(ten, tuoi, gioitinh, diachi)
        self.__congviec = congviec

    def mo_ta(self):
        return f"Nhan vien | Cong viec: {self.__congviec}"

class QLCB:
    def __init__(self):
        self.__ds = []

    def them(self, cb):
        self.__ds.append(cb)
        print(f"Da them: {cb.ten}")

    def tim_ten(self, ten):
        kq = [cb for cb in self.__ds if cb.ten.lower() == ten.lower()]
        if kq:
            for cb in kq: print(cb)
        else:
            print(f"Khong tim thay '{ten}'")

    def hien_thi(self):
        if not self.__ds:
            print("Danh sach rong")
            return
        print("\n--- DANH SACH CAN BO (sap xep A-Z) ---")
        for cb in sorted(self.__ds):   # dung __lt__
            print(cb)                  

    def luu_file(self, ten_file="canbo.txt"):
        with open(ten_file, "w", encoding="utf-8") as f:
            for cb in sorted(self.__ds):
                f.write(f"{cb}\n")
        print(f"Da luu {len(self.__ds)} can bo vao '{ten_file}'")

    def doc_file(self, ten_file="canbo.txt"):
        print(f"\n--- Noi dung file '{ten_file}' ---")
        with open(ten_file, "r", encoding="utf-8") as f:
            for dong in f:
                print(dong.strip())


# Menu 
def nhap_can_bo():
    ten      = input("Ten: ")
    tuoi     = int(input("Tuoi: "))
    gioitinh = input("Gioi tinh: ")
    diachi   = input("Dia chi: ")

    print("a. Cong nhan  b. Ky su  c. Nhan vien")
    loai = input("Chon loai: ").lower()

    if loai == 'a':
        bac = int(input("Bac (1-10): "))
        return CongNhan(ten, tuoi, gioitinh, diachi, bac)
    elif loai == 'b':
        nganh = input("Nganh dao tao: ")
        return KySu(ten, tuoi, gioitinh, diachi, nganh)
    elif loai == 'c':
        cv = input("Cong viec: ")
        return NhanVien(ten, tuoi, gioitinh, diachi, cv)
    else:
        print("Loai khong hop le")
        return None


quanly = QLCB()

while True:
    print("\n--- QUAN LY CAN BO ---")
    print("1. Them moi")
    print("2. Tim kiem theo ten")
    print("3. Hien thi danh sach")
    print("4. Luu file")
    print("5. Doc file")
    print("6. Thoat")

    try:
        chon = int(input("Chon: "))
    except ValueError:
        print("Vui long nhap so")
        continue

    if chon == 6:
        print("Tam biet!")
        break
    elif chon == 1:
        try:
            cb = nhap_can_bo()
            if cb: quanly.them(cb)
        except (TuoiKhongHopLe, BacKhongHopLe) as e:
            print(f"Loi: {e}")
    elif chon == 2:
        quanly.tim_ten(input("Nhap ten: "))
    elif chon == 3:
        quanly.hien_thi()
    elif chon == 4:
        quanly.luu_file()
    elif chon == 5:
        quanly.doc_file()
    else:
        print("Lua chon khong hop le")