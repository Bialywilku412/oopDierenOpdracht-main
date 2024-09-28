# formReadDieren.py
# Anjo Eijeriks
# 2023/11/30 v1

from Dier import Dier  # Import the Dier class from the Dier module

print("Afdrukken alle dieren")

# No need to initialize dierid, soort, and naam here
# They will be passed as parameters to the read_dieren method

# Create an instance of the Dier class
nieuw_dier = Dier(None, None, None)
print("Het object is aangemaakt")

# Retrieve all dieren and store them in the 'dieren' array
dieren = nieuw_dier.read_dieren(None, None, None)

# Check if any dieren are found
if not dieren:
    print("Geen dieren gevonden.")
else:
    # Print information about each dier
    for dier in dieren:
        print(f"Dier ID: {dier[0]}, Soort: {dier[1]}, Naam: {dier[2]}")

