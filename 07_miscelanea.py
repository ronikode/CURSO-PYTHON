"""

3.-
Escriba un programa en python para tomar la decisión de pagar la cuenta en un restaurante:
Si la cuenta es menor a $ 50 pago en efectivo. Sino, si es de $ 50 hasta $ 100 pagaré
con el celular (dinero electrónico). Pero si es mayor a 100 hasta $ 200,
usaré la tarjeta de débito. Caso contrario cancelo con tarjeta de crédito.
"""

customer_a = {"name": "Miguel", "price": 500}
customer_b = {"name": "Javier", "price": 200}
customer_c = {"name": "Dante", "price": 100}

account_restaurant = [customer_a, customer_b, customer_c]

payment = ""
for account in account_restaurant:

    if account.get("price") < 50:
        payment += "\t Efectivo"
    elif account.get("price") == 50 or account.get("price") <= 100:
        payment += "\t Pago desde la app"
    elif 100 < account.get("price") <= 200:
        payment += "\t Tarjeta de débito"
    else:
        payment += "\t Tarjeta de crédito"

print(payment)
