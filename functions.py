'''Gemensamma funktioner'''
import os
import sys
import time

# Platform-specific imports
try:
    import msvcrt  # pylint: disable=import-error,unused-import
except ImportError:
    msvcrt = None  # Not available on Unix/Mac

try:
    import tty  # pylint: disable=import-error,unused-import
    import termios  # pylint: disable=import-error,unused-import
    import select # pylint: disable=import-error,unused-import 
except ImportError:
    tty = None  # Not available on Windows
    termios = None
    select = None

def wait_any_key(non_blocking=False, timeout=3):
    '''press any key function'''
    if os.name == 'nt' and msvcrt:
        if non_blocking:
            if msvcrt.kbhit():
                msvcrt.getch()
                return True
            else:
                time.sleep(timeout)
                return False
        else:
            print("Press any key to return to menu...")
            msvcrt.getch()
            return False
        
    else: #mac/linux
        if tty and termios:
            fd = sys.stdin.fileno()
            
            if non_blocking:
                rlist, _, _ = select.select([sys.stdin], [], [], timeout)
                if rlist:
                    sys.stdin.read(1)
                    return True
                else:
                    return False
            else:
                print("Press any key to return to menu...")
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(fd)
                    sys.stdin.read(1) #Wait for key
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return True

def print_separator(length=30):
    '''Skriver ut en linje med bindestreck'''
    print("=" * length)

def bytes_to_gb(bytes_size):
    '''Convert bytes to GB'''
    return f"{bytes_size / (1024 ** 3):.2f}"

def check_os():
    '''Check which OS is running'''
    if os.name == 'nt':     #windows
        return 'c:\\'
    else:                   #mac/linux
        return '/'
def clean_terminal():
    '''Clear the terminal'''
    os.system('cls' if os.name == 'nt' else 'clear')
