'''System snapshot and setting monitoring'''
import psutil
from functions import bytes_to_gb
from functions import check_os
from functions import wait_any_key
from functions import clean_terminal

def system_snapshot():
    '''Take snapshot of system load'''
    snapshot = True
    while snapshot:
        cpu_usage = psutil.cpu_percent(interval=1)
        disk_info = psutil.disk_usage(check_os())
        ram_info = psutil.virtual_memory()

        used_d = bytes_to_gb(disk_info.used)
        total_d = bytes_to_gb(disk_info.total)
        used_ram = bytes_to_gb(ram_info.used)
        total_ram = bytes_to_gb(ram_info.total)

        clean_terminal()
        print(f"CPU usage:\t {cpu_usage}%  |")
        print(f"DISK usage:\t {disk_info.percent}% | "
                f"{used_d} GB / {total_d} GB.")
        print(f"RAM usage:\t {ram_info.percent}% | "
                f"{used_ram} GB / {total_ram} GB.")
        print("Press any key to return to menu...")
        if wait_any_key(non_blocking=True, timeout=3):
            snapshot = False
            break
        else:
            continue

def start_monitoring():
    '''Set monitoring to True'''
    print("System monitoring started.\nReturning to menu...")
    return True
