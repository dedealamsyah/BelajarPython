'''
Ternary operators dibangun dengan menempatkan "blok kode jika benar" 
pada posisi awal, lalu diikuti oleh "if statement" serta "kondisi"-nya. 
Kemudian "else statement" 
ditempatkan di akhir beserta dengan "blok kode jika salah".

'''

lulus = True
print("selamat") if lulus else print("perbaiki")

"""
Output:
selamat
"""

#jikaFalse

lulus = True
if lulus:
    print("Selamat") 
else:
    print("Perbaiki")

"""
Output:
selamat
"""

#perhatikan bahwa pada ternary tuples kita menggunakan indeks ke-0 tuples sebagai kode jika kondisi salah, 
#sedangkan indeks ke-1 sebagai kode jika kondisi benar. 

lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)

"""
Output:
Selamat, Anda lulus!
"""

# jika kondisi bernilai false. 
#Jika kita ubah menjadi blok kode IF, berikut penerapannya.

lulus = True
if lulus:
    print("Selamat, Anda lulus!") 
else:
    print("Perbaiki, Anda belum lulus.")

"""
Output:
Selamat, Anda lulus!
"""