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
            fd = sys.stdin.fileno() # Get file descriptor for keyboard input (stdin)
            
            if non_blocking:
                rlist, _, _ = select.select([sys.stdin], [], [], timeout) 
                # Use select to wait for timeout(seconds)
                # rlist will contain stdin if key pressed before timeout
                if rlist:
                    sys.stdin.read(1) # Read key press
                    return True
                else:
                    return False # If timeout expired without input
            else:
                print("Press any key to return to menu...")
                old_settings = termios.tcgetattr(fd) # Save current terminal setting
                try:
                    tty.setraw(fd) # Set terminal to raw mode (disable line buffering)
                    sys.stdin.read(1) # Wait for key
                finally:
                    # Restore terminal to previous settings otherwise terminal will be in raw mode
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
