'''Menu-file for main.py'''

from start_monitor import run_monitor
from monitoring import system_snapshot


input_menu = True
while input_menu: 
    menu_choice = input(
        "1. Starta övervakning\n"
        "2. Lista aktiv övervakning\n"
        "3. Skapa larm\n" 
        "4. Visa larm\n" 
        "5. Starta övervakningsläge\n" 
        "6. Avsluta\n")
    if menu_choice == '1':
        run_monitor()
        break
    elif menu_choice == '2':
        system_snapshot()
        break
    else:
        break
