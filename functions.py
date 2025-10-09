'''Gemensamma funktioner'''
import os
import keyboard 


def any_key_press(event):
    '''Press any key function'''
    if event.name == 'esc':
        keyboard.unhook_all()
    else: 
        return

def print_separator(length=30):
    '''Skriver ut en linje med bindestreck'''
    print("=" * length)
#konvertera bytes till gb
def bytes_to_gb(bytes_size):
    '''Convert bytes to GB'''
    return "{:.2f}".format(bytes_size / (1024 ** 3))

def check_os():
    '''Check which OS is running'''
    if os.name == 'nt':     #windows
        return 'c:\\'
    else:                   #mac/linux
        return '/'
