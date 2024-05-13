def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

print(persegi_panjang_pertama)

"""
Output:
50
"""

'''
Kelebihan dari jenis argumen ini adalah walaupun kita harus 
menuliskan lebih banyak kata, urutan parameter fungsi tidak perlu dipikirkan.

'''

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(lebar=10, panjang=5)

print(persegi_panjang_pertama)

"""
Output:
50
"""