'''Huvudprogram'''
from menu import menu_1
from menu import menu_2
from menu import menu_3
from menu import menu_4



def run_menu():
    '''Run the menu'''
    set_monitoring = False
    alarm_list = []
    input_menu = True
    while input_menu:
        menu_choice = input(
            "1. Starta övervakning\n"
            "2. Lista aktiv övervakning\n"
            "3. Skapa larm\n"
            "4. Visa larm\n"
            "5. Starta övervakningsläge\n"
            "6. Avsluta\n")
        match menu_choice:
            case '1':
                set_monitoring = menu_1(set_monitoring)
            case '2':
                set_monitoring = menu_2(set_monitoring)
            case '3':
                alarm_list = menu_3()
            case '4':
                menu_4(alarm_list)
            case '5':
                break
            case _:
                break
run_menu()
