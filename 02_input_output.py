"""
Revision de secion 02

Ingrese su fecha de nacimiento en formato (aaaa-mm-dd)
y que el programa determine sus días vividos, meses y edad.
"""

# Importa la libreria de fecha
from datetime import datetime, timedelta


nacimiento = input("Ingrese su fecha de nacimiento: \n")
today = datetime.now()
start_date = nacimiento.split('-')
year_start_date, month_start_date, day_start_date = start_date[0], start_date[1], start_date[2]

diff_years = today.year - int(year_start_date)
diff_month = today.month - int(month_start_date)
diff_days = today.day - int(day_start_date)

message = f" y edad: {diff_years}"
print(message)

date_1 = today + timedelta(days=30)
print(date_1.strftime("%d/%m/%Y"))