""""
Diccionarios: name = { <key>: <value>}
"""

""""
product_a = {'name': "Laptop A", 'price': 650, 'warehouse': 'A'}
"""
product_a = dict()  # dict()
product_a["name"] = "Laptop A"
product_a['price'] = 650
# product_a['price'] = None
product_a['warehouse'] = "A"

product_b = {"name": "Laptop B", "price": round(1000 / 7, 3), "warehouse": "A"}
product_c = {"name": "ThinkPad Lenovo", "price": round(1200 / 7, 2), "warehouse": "B"}

# Agrupar los productos de la warehouse: A
items_warehouse_a = list()  # []

if product_a.get("warehouse") == "A":
    items_warehouse_a.append(product_a)
if product_b.get("warehouse") == "A":
    items_warehouse_a.append(product_b)
if product_c.get("warehouse") == "A":
    items_warehouse_a.append(product_c)

print(items_warehouse_a)
for item in items_warehouse_a:
    if item.get("price") > 500:
        print(f"Fuera de mi presupuesto: {item.get('name')}")
    else:
        print(f"Si esta dentro de mi presupuesto: {item.get('name')}")

# Obtener la sumtoria de los productos agrupados en  items_warehouse_a
total = 0
for item in items_warehouse_a:
    total = total + item.get("price")  # total += item.get("price")

print("Los productos suman $: ", round(total, 2))
