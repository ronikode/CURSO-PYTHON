"""
Funciones - def <nombre-funcion> (param1, param2):


INPUT                                     OUTPUT
-------> [ def sum_prices_products  ] ----->

"""


def sum_prices_products(items_a: list) -> float:
    """
    Funcion que recibiendo una lista de diccionario calcula la sumatoria
    :param items_a:
    :return total: float:
    """
    total = 0
    for item in items_a:
        total = total + item.get("price")
    return round(total, 2)


product_b = {"name": "Laptop B", "price": round(1000 / 7, 3), "warehouse": "A"}
product_c = {"name": "ThinkPad Lenovo", "price": round(1200 / 7, 2), "warehouse": "A"}
items = list()
items.append(product_b)
items.append(product_c)

totals = sum_prices_products(items_a=items)
print(totals)
