import pandas as pd

# Membuat Dataframe dari dictionary

data = {
    'Nama' : ['Dede','Alamsyah','Silka','Alma'],
    'Usia' : [30, 30, 3, 3],
    'Pekerjaan' : ['Instruktur','Instruktur','Siswa','Siswa']
}

df = pd.DataFrame(data)

#Menampilkan dataframe
print(df)