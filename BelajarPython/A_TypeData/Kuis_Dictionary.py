"""
TODO:
Buatlah variabel dictionary dengan nama "data_diri",
variabel tersebut berisi identitas diri Anda berdasarkan ketentuan berikut.
- Memiliki key bernama "firstName":
    - Isi value dengan nama depan Anda, pastikan bertipe data string.
- Memiliki key bernama "lastName":
    - Isi value dengan nama terakhir Anda, pastikan bertipe data string.
- Memiliki key bernama "age":
    - Isi value dengan umur Anda, pastikan bertipe data integer.
- Memiliki key bernama "isMarried":
    - Isi value dengan status pernikahan Anda, pastikan bertipe data boolean.

Catatan:
- Value pada dictionary harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""


# TODO: Silakan buat kode Anda di bawah ini.
# var dictionary
data_diri = {
    "firstName": "Dede",
    "lastName": "Alamsyah",
    "age": 30,
    "isMarried": False
}

# Tampilkan dari nilai var
print("Data Diri:")
print("Nama depan:", data_diri["firstName"])
print("Nama belakang:", data_diri["lastName"])
print("Umur:", data_diri["age"])
print("Status pernikahan:", data_diri["isMarried"])
