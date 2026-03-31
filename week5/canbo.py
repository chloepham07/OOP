class CanBo:
    def __init__(self, ten, tuoi, gioitinh, diachi):
        self._ten = ten
        self._tuoi = tuoi
        self._gioitinh = gioitinh
        self._diachi = diachi

    def loai_cb(self):
        return "Can bo"

    def thong_tin_rieng(self):
        return ""

    def hien_thi(self):
        print(f"[{self.loai_cb()}] | {self._ten} | {self._tuoi} | {self._gioitinh} | {self._diachi} {self.thong_tin_rieng()}")


class CongNhan(CanBo):
    def __init__(self, ten, tuoi, gioitinh, diachi, bac):
        super().__init__(ten, tuoi, gioitinh, diachi)
        self.__bac = bac

    def loai_cb(self):
        return "Cong nhan"

    def thong_tin_rieng(self):
        return f"| bac: {self.__bac}"


class KySu(CanBo):
    def __init__(self, ten, tuoi, gioitinh, diachi, nganh):
        super().__init__(ten, tuoi, gioitinh, diachi)
        self.__nganh = nganh

    def loai_cb(self):
        return "Ky su"

    def thong_tin_rieng(self):
        return f"| nganh: {self.__nganh}"


class NhanVien(CanBo):
    def __init__(self, ten, tuoi, gioitinh, diachi, congviec):
        super().__init__(ten, tuoi, gioitinh, diachi)
        self.__congviec = congviec

    def loai_cb(self):
        return "Nhan vien"

    def thong_tin_rieng(self):
        return f"| cong viec: {self.__congviec}"


class QLCB:
    def __init__(self):
        self.qlcb = []

    def them_moi_can_bo(self, canbo):
        self.qlcb.append(canbo)
        print("Da them can bo")

    def tim_kiem_theo_ten(self, ten):
        found = False
        for cb in self.qlcb:
            if cb._ten.lower() == ten.lower():
                cb.hien_thi()
                found = True
        if not found:
            print("Khong tim thay")

    def hien_thi_danh_sach(self):
        if len(self.qlcb) == 0:
            print("Danh sach rong")
        else:
            print("\n--- DANH SACH CAN BO ---")
            for cb in self.qlcb:
                cb.hien_thi()


quanly = QLCB()

while True:
    print("\n--- CHUONG TRINH QUAN LY CAN BO ---")
    print("1. Them moi")
    print("2. Tim kiem")
    print("3. Hien thi danh sach")
    print("4. Thoat")

    chon = int(input("Chon so tuong ung: "))

    if chon == 4:
        print("Tam biet")
        break

    elif chon == 1:
        ten = input("Ten: ")
        tuoi = int(input("Tuoi: "))
        gioitinh = input("Gioi tinh: ")
        diachi = input("Dia chi: ")

        print("a. Cong nhan | b. Ky su | c. Nhan vien")
        loai = input("Chon loai: ")

        if loai == 'a':
            bac = int(input("Bac: "))
            quanly.them_moi_can_bo(CongNhan(ten, tuoi, gioitinh, diachi, bac))

        elif loai == 'b':
            nganh = input("Nganh: ")
            quanly.them_moi_can_bo(KySu(ten, tuoi, gioitinh, diachi, nganh))

        elif loai == 'c':
            cv = input("Cong viec: ")
            quanly.them_moi_can_bo(NhanVien(ten, tuoi, gioitinh, diachi, cv))

        else:
            print("Lua chon khong hop le")

    elif chon == 2:
        ten = input("Nhap ten can tim: ")
        quanly.tim_kiem_theo_ten(ten)

    elif chon == 3:
        quanly.hien_thi_danh_sach()

    else:
        print("Lua chon khong hop le")