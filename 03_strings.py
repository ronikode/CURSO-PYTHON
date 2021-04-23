""""
Strings en python
"""
store_a = "Store A"
store_b = 'Store B'

# Uppercase
print(store_a.upper())

# Capitalize
store_review = "revisiones de curso python"
print(store_review.title())

# Lowercase
print(store_b.lower())

# Coleccion
#  0  1  2  3  4  5 6
# [s][t][o][r][e][][A]
print(len(store_a))
print(store_a[2])
# print(store_a[10]) # IndexError
print(store_a[-1])
print(store_b[-2])

# Slicing | Dividir tu cadena de caracteres desde y hasta
sub_store_a = store_a[0:4]
print(sub_store_a)

store_d = "Store 12"
sub_store_d = store_d[:-1]  # Store 1
sub_store_e = sub_store_d[6:]
print(int(sub_store_e))

if "12" in store_a:  # Sentencia de control if (condicion) :
    print("Lo encontro")
else:
    print("No lo tiene")

# { }
