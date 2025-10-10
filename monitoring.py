'''System snapshot and setting monitoring'''
import psutil
from functions import bytes_to_gb
from functions import check_os
from functions import print_separator

def system_snapshot():
    '''Take snapshot of system load'''
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_info = psutil.disk_usage(check_os())
    ram_info = psutil.virtual_memory()

    #convert bytes to GB
    used_d = bytes_to_gb(disk_info.used)
    total_d = bytes_to_gb(disk_info.total)
    used_ram = bytes_to_gb(ram_info.used)
    total_ram = bytes_to_gb(ram_info.total)

    # Top frame
    print_separator(50)

    print(f"CPU-användning: {cpu_usage}% |")
    print(f"Diskanvändning: {disk_info.percent}% | "
            f"{used_d} GB / {total_d} GB.")
    print(f"RAM-användning: {ram_info.percent}% | "
            f"{used_ram} GB / {total_ram} GB.")

    # Bottom frame
    print_separator(50)

    return
#system_snapshot()

def start_monitoring():
    '''Set monitoring to True'''
    print("System monitoring started.\nReturning to menu...")
    return True
