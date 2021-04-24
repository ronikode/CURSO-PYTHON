""""
Ejemplo programacion estructurada
"""

customers = [
    {"name": "Roberto", "last_name": "Noboa", "dni": "1111111111"},
    {"name": "Juan", "last_name": "Gonzales", "dni": "999999999"}
]

""""
Ejemplo programacion orientada a objetos
"""


def search_customer_by_dni(data: list, dni: str) -> dict:
    resp = {}
    for customer in data:
        if dni == customer.get("dni"):
            resp = customer
    return resp


"""POO"""


# class <name_class>:
class Customer:

    def __init__(self, name: str, last_name: str, dni: str, budget: float = 0):  # Constructor
        self.name = name
        self.last_name = last_name
        self.dni = dni
        self.budget = budget

    def __str__(self):
        return f"[{self.dni}] - {self.name} {self.last_name}"

    # Metodo de instancia
    def search_customer_dni(self, data: list) -> 'Customer':
        for el in data:
            if el.dni == self.dni:
                return el
        return None

    # Metodo estaticos


c1 = Customer(name="Roberto", last_name="Noboa", dni="1111111111")
data_c2 = {"name": "Juan", "last_name": "Gonzales", "dni": "999999999"}
c2 = Customer(**data_c2)

customers_object = [
    Customer(name="Javier", last_name="B", dni="12312345"),
    c2,
    Customer(name="Nico", last_name="Noboa", dni="129876540")
]

target_c = c1.search_customer_dni(data=customers_object)
if target_c is None:
    print("No lo encuentra")
