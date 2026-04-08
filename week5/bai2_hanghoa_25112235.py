class HangHoa:
    def __init__(self, mahang, tenhang, nhasx, gia):
        self.mahang = mahang
        self.tenhang = tenhang
        self.nhasx = nhasx
        self.gia = gia

    def thong_tin_rieng():
        return ""

    def hien_thi(self):
        print(f" {self.mahang} | {self.tenhang} | {self.nhasx} | {self.gia} | {self.thong_tin_rieng()}")

class HangDienMay(HangHoa):
    def __init__(self, mahang, tenhang, nhasx, gia, tgbh, dienap, congsuat):
        super().__init__( mahang, tenhang, nhasx, gia)
        self.tgbh = tgbh
        self.dienap = dienap
        self.congsuat = congsuat

    def thong_tin_rieng(self):
        return f"thoi gian bao hanh: {self.tgbh} | dien ap: {self.dienap} | cong suat: {self.congsuat} "
    
class HangSanhSu(HangHoa):
    def __init__(self, mahang, tenhang, nhasx, gia, loainguyenlieu):
        super().__init__(mahang, tenhang, nhasx, gia)
        self.loainguyenlieu = loainguyenlieu

    def thong_tin_rieng(self):
        return f"loai nguyen lieu: {self.loainguyenlieu} "
    
class HangThucPham(HangHoa):
    def __init__(self, mahang, tenhang, nhasx, gia, nsx, hsd):
        super().__init__( mahang, tenhang, nhasx, gia)
        self.nsx = nsx
        self.hsd = hsd

    def thong_tin_rieng(self):
        return f"ngay san xuat: {self.nsx} | han su dung: {self.hsd}"
    
hh1 = HangDienMay('001','dieu hoa','panasony', 2000, '2 nam', 220 ,1000)
hh2 = HangSanhSu('002', 'bat', 'bat trang', 30, 'gom su')
hh3 = HangThucPham ('003' ,'kem' ,'abc' ,2, '1/4', '5/4')

hh1.hien_thi()
hh2.hien_thi()
hh3.hien_thi()

    

    

