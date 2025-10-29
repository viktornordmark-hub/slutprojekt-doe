'''Huvudprogram'''
import logging
from menu import menu_1, menu_2, menu_3, menu_4, menu_5, menu_6
from functions import clean_terminal

logging.basicConfig(
    filename='program.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

def run_menu():
    '''Run the menu'''
    logging.info("Program started. Show menu")
    set_monitoring = False
    alarm_list = []
    input_menu = True
    while input_menu:
        menu_choice = input(
            "1. Start monitoring\n"
            "2. List active monitoring\n"
            "3. Create alarm\n"
            "4. Show alarm\n"
            "5. Start monitor mode\n"
            "6. Remove alarm\n"
            "7. Exit\n")
        match menu_choice:
            case '1':
                set_monitoring = menu_1(set_monitoring)
            case '2':
                set_monitoring = menu_2(set_monitoring)
            case '3':
                alarm_list = menu_3(alarm_list)
            case '4':
                menu_4(alarm_list)
            case '5':
                menu_5(alarm_list, set_monitoring)
            case '6':
                menu_6(alarm_list)
            case '7':
                logging.info("Exit program")
                clean_terminal()
                print("Program exits.")
                break
            case _:
                logging.info("Invalid input in menu")
                clean_terminal()
                print("Please choose 1-7!")

def main():
    '''Run program'''
    run_menu()

if __name__ == "__main__":
    main()
