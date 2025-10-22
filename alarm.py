'''Handle and create alarms'''
#import time
from functions import clean_terminal

class Alarm:
    '''class alarm'''
    def __init__(self, alarm_type, threshold: int):
        self.alarm_type = alarm_type #cpu, ram, disk
        self.threshold  = threshold #warning %
        self.triggered = False #if alarm triggered

    def check_trigger(self, current_value: float) -> bool:
        '''Return True to trigger alarm'''
        if current_value > self.threshold:
            self.triggered = True
            return True
        else:
            return False
            
    def __str__(self):
        '''Print alarm message'''
        return (
            f"{self.alarm_type.upper()}: {self.threshold}% "
            f"{'\033[1;3;31mWARNING ALARM TRIGGERED\033[0m' if self.triggered else ''}"
        )
alarm_list = []

def create_some_alarms():
    '''create alarm and store in list'''
    create_alarm = True
    while create_alarm:      
        while True:
            alarm_type = input("Configure alarm.\n1. CPU\n2. DISK\n3. RAM\n4. Return to menu\n: ")
            match alarm_type:
                case '1':
                    alarm_type = 'CPU'
                    break
                case '2':
                    alarm_type = 'DISK'
                    break
                case '3':
                    alarm_type = 'RAM'
                    break
                case '4':
                    create_alarm = False
                    break
                case _:
                    print("Please choose number 1-4!")
                    continue
        if not create_alarm:
            clean_terminal()
            break

        while create_alarm:
            try:
                threshold = int(input("Choose warning level (1-100):\n"))
                if threshold < 1 or threshold > 100:
                    print("Input must be between 1-100!")
                    continue
                else:
                    break
            except ValueError:
                print("Input must be number 1-100!")
        clean_terminal()
        new_alarm = Alarm(alarm_type, threshold)
        alarm_list.append(new_alarm)
        print(f"Alarm created: {alarm_type} at {threshold}%\n")

    return alarm_list


