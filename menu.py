'''Menu-file for main.py'''
import os
import keyboard
from start_monitor import run_monitor
from monitoring import system_snapshot
from functions import any_key_press


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
        print("System monitoring started.\nReturning to menu...") 
        continue
    elif menu_choice == '2':
        system_snapshot()
        input("Press enter to confirm: ")
        print("Press any key to return to menu...")
        keyboard.read_key()
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        break
