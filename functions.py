'''Gemensamma funktioner'''
import os
import sys

# Platform-specific imports
try:
    import msvcrt  # pylint: disable=import-error,unused-import
except ImportError:
    msvcrt = None  # Not available on Unix/Mac

try:
    import tty  # pylint: disable=import-error,unused-import
    import termios  # pylint: disable=import-error,unused-import
except ImportError:
    tty = None  # Not available on Windows
    termios = None


def wait_any_key():
    '''press any key function'''
    if os.name == 'nt': #windows
        if msvcrt:
            print("Press any key to return to menu...")
            msvcrt.getch() #Wait for any key
    else: #mac/linux
        if tty and termios:
            print("Press any key to return to menu...")

            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                sys.stdin.read(1) #Wait for key
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def print_separator(length=30):
    '''Skriver ut en linje med bindestreck'''
    print("=" * length)
#konvertera bytes till gb
def bytes_to_gb(bytes_size):
    '''Convert bytes to GB'''
    return f"{bytes_size / (1024 ** 3):.2f}"

def check_os():
    '''Check which OS is running'''
    if os.name == 'nt':     #windows
        return 'c:\\'
    else:                   #mac/linux
        return '/'
