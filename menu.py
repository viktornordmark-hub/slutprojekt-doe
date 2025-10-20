'''Menu-file for main.py'''
import time
from monitoring import start_monitoring
from monitoring import system_snapshot
from functions import wait_any_key
from functions import clean_terminal
from alarm import create_some_alarms
def menu_1(set_monitoring):
    '''Menu choice 1'''
    if set_monitoring is True:
        print("System monitoring already active!")
        input("Press enter to confirm...")
        clean_terminal()
        return True
    else:
        set_monitoring = start_monitoring()
        time.sleep(3)
        clean_terminal()
        return True

def menu_2(set_monitoring):
    '''Send system snapshot if monitoring active'''
    if set_monitoring is False:
        print("System monitoring not active!")
        input("Press enter to return to menu: ")
        clean_terminal()
        return False
    else:
        system_snapshot()
        input("Press enter to confirm: ")
        wait_any_key()
        clean_terminal()
        return True

def menu_3():
    '''create alarms'''
    return create_some_alarms()

def menu_4(alarm_list):
    '''show alarms'''
    if not alarm_list:
        print("No alarms created yet!")
        input("Press enter to continue...")
    else:
        for alarm_obj in alarm_list:
            print(alarm_obj)
        input("Press enter to continue...")
    clean_terminal()

def menu_5():
    '''Surveliance mode'''
    

