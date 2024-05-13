def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))
"""
Output:
nama: Dicoding, usia: 17, pekerjaan: Python Programmer,
"""