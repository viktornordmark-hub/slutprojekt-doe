#Lista aktiv övervakning
import time
import os
import psutil
from functions import bytes_to_gb


'''if os.name == 'nt':     #windows
    path_disc = 'c:\\'
else:                   #mac/linux
    path_disc = '/'
    '''


try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        disk_info = psutil.disk_usage(path_disc)
        ram_info = psutil.virtual_memory()
        #konvertera avända bytes till gb
        used_d = bytes_to_gb(disk_info.used)
        total_d = bytes_to_gb(disk_info.total)
        used_ram = bytes_to_gb(ram_info.used)
        total_ram = bytes_to_gb(ram_info.total)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\rCPU-användning: {cpu_usage}%")
        print(f"Diskanvändning: {disk_info.percent}% " #procent av diskanvändning
              f"{used_d} GB av {total_d} GB tillgängligt.")
        print(f"RAM-användning: {ram_info.percent}% " #procent av ramanvändning
              f"{used_ram} GB av {total_ram} GB tillgängligt.", end="\r\n")
        time.sleep(0.1)
except KeyboardInterrupt:
        print("\nAborting...")
