#Starta övervakning
import psutil

def run_monitor():
    running = True
    while run_monitor:
        cpu_usage = psutil.cpu_percent(interval=1) 
        disk_info = psutil.disk_usage('C:\\')
        ram_info = psutil.virtual_memory()
