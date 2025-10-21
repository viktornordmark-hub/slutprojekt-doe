'''Huvudprogram'''
from menu import menu_1
from menu import menu_2
from menu import menu_3
from menu import menu_4
from menu import menu_5
from functions import clean_terminal


def run_menu():
    '''Run the menu'''
    set_monitoring = False
    alarm_list = []
    input_menu = True
    while input_menu:
        menu_choice = input(
            "1. Start monitoring\n"
            "2. List active monitoring\n"
            "3. Create larm\n"
            "4. Show larm\n"
            "5. Start monitor mode\n"
            "6. Exit\n")
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
                menu_5(alarm_list)
            case '6':
                clean_terminal()
                print("Program exits.")
                break
            case _:
                clean_terminal()
                print("Please choose 1-6!")
run_menu()
