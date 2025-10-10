'''import time 
import psutil
import os

if os.name == 'nt':     #windows
    path_disc = 'c:\\'
else:                   #mac/linux
    path_disc = '/'

def display_usage(cpu_usage, mem_usage, disk_usage, bars=50):
    cpu_percent = cpu_usage / 100.0
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars)) 
    #alt code symbol (alt 219)

    mem_percent = mem_usage / 100.0
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    disk_percent = disk_usage / 100.0
    disk_bar = '█' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}% ", end="")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}% ", end="")
    print(f"Disk usage: |{disk_bar}| {disk_usage:.2f}% ", end="\r")

print("Press 'Ctrl + c' to abort...")

try: 
    while True:
        display_usage(
            psutil.cpu_percent(), 
            psutil.virtual_memory().percent, 
            psutil.disk_usage(path_disc).percent, 30)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("\nAborting...")  

#os.system('cls' if os.name == 'nt' else 'clear')

psutil.cpu_percent(interval=1)
psutil.disk_usage(check_os())
psutil.virtual_memory()
time.sleep(1)
'''
