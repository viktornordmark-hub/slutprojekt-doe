#Lista aktiv övervakning
import psutil
import os
from functions import bytes_to_gb 

if os.name == 'nt':     #windows
    path_disc = 'c:\\'
else:                   #mac/linux
    path_disc = '/'

cpu_usage = psutil.cpu_percent(interval=1) 
disk_info = psutil.disk_usage(path_disc)
ram_info = psutil.virtual_memory()

used_d = bytes_to_gb(disk_info.used) #konvertera använda bytes till gb
total_d = bytes_to_gb(disk_info.total) #konvertera totala bytes till gb

used_ram = bytes_to_gb(ram_info.used)
total_ram = bytes_to_gb(ram_info.total)

print(f"CPU-användning: {cpu_usage}%")
print(f"Diskanvändning: {disk_info.percent}% " #procent av diskanvändning
      f"({used_d} GB av {total_d} GB tillgängligt.)")
print(f"RAM-användning: {ram_info.percent}% " #procent av ramanvändning
      f"({used_ram} GB av {total_ram} GB tillgängligt.)")

