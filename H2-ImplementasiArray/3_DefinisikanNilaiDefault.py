var_arr = [0 for i in range(10)]
print(var_arr)

"""
Output:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""

#Dari sini, Anda dapat mengubah nilai default tersebut dengan nilai yang baru berdasarkan hasil suatu operasi. 
#Misalkan pada contoh di bawah ini.

var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)


"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""