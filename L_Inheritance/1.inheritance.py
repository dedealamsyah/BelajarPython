class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

"""
Output:
160
"""

'''
Pada contoh di atas, kita membuat sebuah kelas bernama Mobil dengan atributnya adalah warna, merek, dan kecepatan. 
Kelas ini juga memiliki metode, yaitu tambah_kecepatan untuk meningkatkan kecepatan mobil sebesar 10. 
Anggap bahwa kode ini tidak boleh diubah sama sekali.

Kita akan membuat sebuah kelas baru bernama "MobilSport" yang mewarisi atribut dan metode kelas Mobil dasar. 
Lalu, kita menambahkan metode baru, yaitu turbo untuk meningkatkan kecepatan sebesar 50.

'''
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

"""
Output:
160
160
210
"""