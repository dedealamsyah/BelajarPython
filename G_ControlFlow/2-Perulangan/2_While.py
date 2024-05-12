counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment

"""
Output:
1
2
3
4
5
"""

'''
Namun, Anda harus berhati-hati untuk tidak melakukan infinite loop, 
yakni sebuah kondisi ketika perulangan tidak berhenti karena 
tidak memenuhi kondisi yang diinginkan. 
Contohnya adalah ketika melakukan perulangan, 
kita tidak memberikan increment yang menyebabkan variabel atau 
counter tidak akan memenuhi kondisi while.

'''