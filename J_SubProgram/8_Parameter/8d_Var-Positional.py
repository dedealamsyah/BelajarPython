def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

"""
Output:
<class 'tuple'>
6
"""

print(hitung_total(1, 2, 3, 4, 5, 6, 7, 8))
