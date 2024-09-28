# formDeleteDier.py
# Anjo Eijeriks
# 2023/11/30 v1

from Dier import Dier               # omdat we OOP doen
print("Verwijder dier")

dierid = input("Welk dierid wil je verwijderen? ")                
soort = None                        # soort en naam zijn niet nodig
naam = None

verwijder_dier = Dier(dierid, soort, naam)
print("Het object is aangemaakt")

# eerst gaan we het dier zoeken
# het gevonden dier komt in de array 'dieren'
# TIK HIER JE EIGEN CODE ..........................
# .................................................

for dier in dieren:
    print(f"Dier ID: {dier[0]}, Soort: {dier[1]}, Naam: {dier[2]}")
    dierid = dier[0]
# Get user input to determine if the user wants to delete the dier
antwoord = input("Wil je dit dier verwijderen? j/n ").lower()

if antwoord == "j":
    # User confirmed deletion
    verwijder_dier.delete_dier(dierid)
    print(f"Dier met dierid {dierid} is verwijderd.")
    
    # TIK HIER JE EIGEN CODE (after deletion) .........
    # For example, you might want to update the display or perform other actions
    
    # Example: Refresh the list of dieren after deletion
    refreshed_dieren = verwijder_dier.read_dieren()
    for dier in refreshed_dieren:
        print(f"Updated Dier ID: {dier[0]}, Soort: {dier[1]}, Naam: {dier[2]}")
    
    # .................................................

else:
    # User chose not to delete the dier
    print("Dier is niet verwijderd.")
    
    # TIK HIER JE EIGEN CODE (if not deleted) .........
    # For example, you might want to display a message or perform other actions
    
    # Example: Display a message or prompt the user for additional actions
    print("Geen wijzigingen aangebracht.")
    
    # .................................................
