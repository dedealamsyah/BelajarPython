var_list = [1,2,3]
for elemen in var_list:
    print(id(elemen))

    '''
    Ketika Anda menjalankan kode di atas, ia akan menghasilkan lokasi memori 
    setiap elemen yang berada pada list. Lokasi tersebut bisa berubah jika 
    Anda menjalankan ulang program, tetapi perhatikan bahwa semua elemen 
    tersebut memiliki ID lokasi penyimpanan yang berbeda.
    '''

    