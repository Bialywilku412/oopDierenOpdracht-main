# formCreateDier.py
# Anjo Eijeriks
# 2023/11/29 v1

from Dier import Dier               # omdat we OOP doen
print("Invoeren nieuw dier")
dierid = None                       # niet nodig, tabel is autoincrement
soort = input("Wat voor soort? ")
naam = input("Wat voor naam? ")
print("")

nieuw_dier = Dier(dierid, soort, naam)
print("Het object is aangemaakt")

nieuw_dier.create_dier(dierid, soort, naam)
print(f"soort: {soort}, naam: {naam} is in de tabel gezet")

