"""

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
