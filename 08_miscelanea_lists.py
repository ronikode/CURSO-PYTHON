"""
4.-) La lista mostrada en el ejemplo contiene URLs de diferentes sitios web que han sido visitados.
Las URLs normalmente se repiten y corresponden algunas veces a universidades de Ecuador y otros países.
Note que los URLs no diferencian entre mayúsculas y minúsculas.

Escriba un programa en python que realice lo siguiente:

A. Muestre los nombres o siglas de las universidades que aparecen en la lista (sin repetir).
B. Muestre la cantidad y nombres/siglas de universidades de Ecuador que aparecen en la lista.

"""

universities = [
    "www.espol.edu.ec", "www.google.com", "www.sri.gob.ec", "www.fiec.espol.edu.ec",
    "www.uees.edu.ec", "www.FIEC.espol.edu.ec", "www.fict.espol.edu.ec",
    "www.fcnm.Espol.edu.ec", "www.ucsg.edu.ec", "www.Standford.edu", "www.harvard.edu",
    "www.standford.edu", "www.google.com.ec", "www.elnoticiero.com.ec", "www.opensource.org",
    "www.facebook.com", "www.UCSG.edu.ec"
]

siglas = []
u_ecuador = []
for uni in universities:
    if 'edu' in uni:
        lst_uni = uni.split(".")
        index = lst_uni.index('edu')  # Devuelve un entero de donde esta el elemento.
        university = str(lst_uni[index - 1]).upper()
        if university not in siglas:
            siglas.append(university)
        if university not in u_ecuador and 'ec' in uni:
            u_ecuador.append(university)

# A
print(f"Tenemos {len(siglas)} universidades: \n")
for i in siglas:
    print(f"\t{i}")

# B
print(f"Tenemos {len(u_ecuador)} universidades de ecuador: \n")
for i in u_ecuador:
    print(f"\t{i}")