angka = [ 10, 20, 30, 40, 50, 60, 70, 80, 90 ]
print(angka)

"""
parameter = [start : stop : step]
[start,stop] = diambil dari index
[step] = lompatannya

contoh untuk menghasilkan data 
[10, 20, 30, 40]
maka masukan parameternya adalah
[start] = 0
[stop] = index terakhir + 1
[step] = optional, default=1

"""
print(angka[:4:1])

'contoh data [50, 60, 70, 80. 90]'

print(angka[:4:9])

'contoh data [20, 40, 60, 80]'

print(angka[1:8:2])