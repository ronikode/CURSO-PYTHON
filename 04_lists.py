"""
Listas
"""

lst1 = [1, "Curso Python", 100.50]

# Basado en la lista 'items' armar mensaje con los nombres de los productos en mayuscula

items = ['Laptop A', "Laptop B", "Disco externo b", 100]
message = ""

# a)
# for <varibale> in <colleccion>

for item in items:
    if isinstance(item, int):
        pass
    else:
        message = str(message + f"\t {item}").upper()
print(message)