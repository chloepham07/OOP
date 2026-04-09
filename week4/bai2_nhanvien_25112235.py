class NhanVien():
    def __init__(self,tenNhanVien, luongCoBan: float, heSoLuong : float, Luong_Max : float):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong
        if luongCoBan < 0: 
            raise ValueError("Lương không âm")
        self.__luongCoBan = min(luongCoBan, Luong_Max)
        self.Luong_Max = Luong_Max
        
    def get_tenNhanVien(self):
        return self.__tenNhanVien
    
    def get_luongCoBan(self):
        return self.__luongCoBan
    
    def get_heSoLuong(self):
        return self.__heSoLuong
    
    def set_tenNhanVien(self, ten_moi):
        self.__tenNhanVien = ten_moi

    def set_luongCoBan(self, luong_moi):
        self.__luongCoBan = luong_moi

    def set_heSoLuong(self, heSoLuong_moi):
        self.__heSoLuong = heSoLuong_moi

    def tinhLuong(self):
        luong = self.__luongCoBan * self.__heSoLuong
        return luong
    
    def inTTin(self):
        print( f"ten: {self.__tenNhanVien} | luong co ban: {self.__luongCoBan }| he so luong: {self.__heSoLuong}| luong max: {self.Luong_Max}| luong : {self.tinhLuong()}")
    
    def tangLuong(self, heSoTang) -> bool:
        heSoMoi = heSoTang + self.__heSoLuong
        luong_moi = heSoMoi * self.__luongCoBan
        if luong_moi > self.Luong_Max:
            print("khong duoc phep thay doi")
            return False
        else:
            self.__heSoLuong = heSoMoi
            print(f"Luong moi: {luong_moi}")
            return True
        
nv1 = NhanVien('Duyen', 100, 3, 1000)
nv1.inTTin()
nv1.tangLuong(1)
nv1.inTTin()

