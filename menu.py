'''Menu-file for main.py'''
import os
import time
from start_monitor import run_monitor
from monitoring import system_snapshot
from functions import wait_any_key

def run_menu():
    '''Run the menu'''
    start_monitoring = False
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
            start_monitoring = True
            run_monitor()
            print("System monitoring started.\nReturning to menu...")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif menu_choice == '2':
            if start_monitoring is False:
                print("System monitoring not active!")
                input("Press enter to return to menu: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            else:
                system_snapshot()
                input("Press enter to confirm: ")
                wait_any_key()
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

        else:
            break
