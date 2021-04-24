""""
Clase de cliente
"""


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
