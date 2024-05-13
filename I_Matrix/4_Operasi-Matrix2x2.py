'''
Pada ilustrasi tersebut, kita mengalikan matriks "[5, 0], [1, -2]" 
dengan konstanta "2". Nilai konstanta tersebut kemudian dikalikan 
dengan setiap elemen matriks. 
Kalkulasinya dapat kita urai seperti berikut. 
'''

# Membuat matriks 2x2
var_mat = [[5, 0],
          [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
    def_mat[i][j] = var_mat[i][j]*2

print(def_mat)

"""
Output:
[[10, 0], [2, -4]]
"""