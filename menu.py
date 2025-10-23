'''Menu functions for main.py'''
import logging
import time
from typing import List
import psutil
from monitoring import start_monitoring
from monitoring import system_snapshot
from functions import wait_any_key
from functions import clean_terminal
from functions import check_os
from alarm import create_some_alarms
from alarm import Alarm

def menu_1(set_monitoring):
    '''Menu choice 1'''
    clean_terminal()
    if set_monitoring is True:
        logging.info("[Menu 1] Monitoring already active")
        print("System monitoring already active!")
        input("Press enter to confirm...")
        clean_terminal()
        return True
    else:
        logging.info("User select 1. Start monitoring")
        set_monitoring = start_monitoring()
        time.sleep(3)
        clean_terminal()
        return True

def menu_2(set_monitoring):
    '''Send system snapshot if monitoring active'''
    clean_terminal()
    if set_monitoring is False:
        logging.info("[Menu 2] Monitoring not active")
        print("System monitoring not active!")
        input("Press enter to return to menu: ")
        clean_terminal()
        return False
    else:
        logging.info("User select 2. List active monitoring")
        system_snapshot()
        clean_terminal()
        return True

def menu_3(alarm_list):
    '''create alarms'''
    logging.info("User select 3. Create alarm")
    clean_terminal()
    return create_some_alarms(alarm_list)


def menu_4(alarm_list: List[Alarm]):
    '''show alarms'''
    logging.info("User select 4. Show alarm")
    clean_terminal()
    if not alarm_list:
        print("No alarms created yet!")
        input("Press enter to continue...")
    else:
        print("===Active Alarms===")
        sorted_active_alarms = sorted(alarm_list, key=lambda a: a.alarm_type)
        for i, alarm_obj in enumerate(sorted_active_alarms):
            print(f"[{i+1}] {alarm_obj}")
        input("Press enter to continue...")
    clean_terminal()

def menu_5(alarm_list: List[Alarm], set_monitoring):
    '''Surveillance mode'''
    logging.info("User select 5. Start monitor mode")
    clean_terminal()
    if set_monitoring is False:
        logging.info("[Menu 5] Monitoring not active")
        print("Monitoring is not active!")
        input("Press enter to return to menu")
        return False
    
    print("Surveillance mode active!")
    time.sleep(3)
    clean_terminal()
    surv_mode = True

    while surv_mode:
        clean_terminal()
        cpu_usage = psutil.cpu_percent(interval=1)
        disk_percent = psutil.disk_usage(check_os()).percent
        ram_percent = psutil.virtual_memory().percent

        for alarm in alarm_list:
            if alarm.alarm_type == 'CPU' and alarm.check_trigger(cpu_usage):
                print(alarm)
            elif alarm.alarm_type == 'DISK' and alarm.check_trigger(disk_percent):
                print(alarm)
            elif alarm.alarm_type == 'RAM'and alarm.check_trigger(ram_percent):
                print(alarm)

        print("Monitoring active...\nPress any key to return to menu: ")
        if wait_any_key(non_blocking=True, timeout=3):
            surv_mode = False
            clean_terminal()
            logging.info("User returned to menu")
            break

def menu_6(alarm_list: List[Alarm]):
    '''Remove alarm'''
    logging.info("User selected 6. Remove alarm")
    clean_terminal()
    if not alarm_list:
        logging.info("No alarms to remove")
        print("No active alarms!\nReturning to menu...")
        time.sleep(3)
        clean_terminal()
        return
    
    while True:
        print("===Current Alarms===")
        sorted_alarms = sorted(alarm_list, key=lambda a:a.alarm_type)
        for i, alarm in enumerate(sorted_alarms):
            print(f"[{i+1}] {alarm}")
        alarm_to_remove = input(
            f"Which alarm would you like to remove? 1-{len(alarm_list)}\n"
            "Press enter to return to menu\n").strip()
        if not alarm_to_remove.isdigit():
            logging.info("User returned to menu")
            break
        try:
            index_to_remove = int(alarm_to_remove)
            list_index = index_to_remove - 1
            if 0 <= list_index < len(alarm_list):
                removed_alarm = alarm_list.pop(list_index)
                clean_terminal()
                logging.info("Removed alarm: %s at %s%%",
                             removed_alarm.alarm_type, removed_alarm.threshold)
                print(f"{removed_alarm.alarm_type} alarm at {removed_alarm.threshold}% removed.")
                if not alarm_list:
                    logging.info("All alarms removed")
                    print("All alarms removed. Returning to menu...")
                    time.sleep(3)
                    break
            else:
                clean_terminal()
                print(f"Invalid choice. Please enter a number between 1 and {len(alarm_list)}!")
        except ValueError:
            print("Invalid input. Please enter a valid number or return to menu.")
    clean_terminal()
