# menu.py
# Anjo Eijeriks
# 2023/11/23 v3

import os                           # nodig voor regel 14
from Dier import Dier               # omdat we OOP doen
import subprocess                   # we starten andere Python programma's

doorgaan = True                     # programma werkt in een eeuwigdurende lus
while doorgaan:
        # AFDRUKKEN MENU
        # de volgende regel maakt het scherm schoon
        # dat werkt alleen bij het dosvenster of Linux terminal
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("")
        print("Menu dierentuin")
        print("1. Create dier")
        print("2. Read dieren")
        print("3. Update dier")
        print("4. Delete dier")
        print("5. Search dier")
        print("0. Stoppen")         # de manier om het programma te beëindigen

        # MENUKEUZEN
        choice = input("Typ je keuze: ")
        if choice =="0":
                print("Het programma is gestopt")
                break
        elif choice =="1":
                # bij keuze 1 start je het programma formCreateDier.py
                subprocess.run(['python', 'formCreateDier.py'])
        elif choice =="2":
               subprocess.run(['python', 'formReadDieren.py'])
        elif choice =="3":
               subprocess.run(['python', 'formUpdateDier.py'])
        elif choice =="4":
                subprocess.run(['python', 'formDeleteDier.py'])
        elif choice =="5":
                subprocess.run(['python', 'formSearchDier.py'])
        else:
                print("Tik 1,2,3,4,5 of 0")
                
        input("Druk op <enter>")
        

              
                
        
        
