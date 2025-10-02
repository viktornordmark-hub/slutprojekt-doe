#Huvudprogram
#Meny

from functions import print_heading

print_heading("Välkommen till programmet")
print_heading("MENY")


input_menu = True
while input_menu: 
    menu_choice = input("1. Starta övervakning\n2. Lista aktiv övervakning\n" \
    "3. Skapa larm\n4. Visa larm\n5. Starta övervakningsläge\n6. Avsluta")
