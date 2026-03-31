class PhongBan:
    def __init__(self, ma_nv, ten, namsinh, gioitinh, diachi, hesoluong, luongtoida):
        self.ma_nv = ma_nv
        self.ten = ten
        self.namsinh = namsinh
        self.gioitinh = gioitinh
        self.diachi = diachi
        self.hesoluong = hesoluong
        self.luongtoida = luongtoida

    def tinh_luong(self):
        return self.hesoluong * self.luongtoida
    
    def hien_thi(self):
        print(f"{self.ma_nv} | {self.ten} | Luong: {self.tinh_luong()}")


class CongTacVien(PhongBan):
    def __init__(self,ma_nv, ten, namsinh, gioitinh, diachi, hesoluong, luongtoida, thoihan, phucap):
        super().__init__(ma_nv, ten, namsinh, gioitinh, diachi, hesoluong, luongtoida)
        self.thoihan = thoihan
        self.phucap = phucap

    def tinh_luong(self):
        return super().tinh_luong() + self.phucap
    
class NhanVienChinhThuc(PhongBan):
    def __init__(self,ma_nv, ten, namsinh, gioitinh, diachi, hesoluong, luongtoida, vitri):
        super().__init__(ma_nv, ten, namsinh, gioitinh, diachi, hesoluong, luongtoida)
        self.vitri = vitri

class TruongPhong(PhongBan):
    def __init__(self,ma_nv, ten, namsinh, gioitinh, diachi, hesoluong, luongtoida, ngaybatdau, phucapql):
        super().__init__(ma_nv, ten, namsinh, gioitinh, diachi, hesoluong, luongtoida)
        self.ngaybatdau = ngaybatdau
        self.phucapql = phucapql

    def tinh_luong(self):
        return super().tinh_luong() + self.phucapql
    
nv1 = CongTacVien('001', 'duyen', '2007', 'nu', 'nd' ,10,1000, '6 thang', 400)
nv2 = NhanVienChinhThuc('002', 'meo', '2004', 'nu' ,'nd', 4, 4000, 'vp')

nv1.hien_thi()
nv2.hien_thi()
    
    


