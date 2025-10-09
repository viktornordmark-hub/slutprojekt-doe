#Starta övervakning
import time
import psutil
#from functions import bytes_to_gb
from functions import check_os


def run_monitor():
    try:
        while True:
            psutil.cpu_percent(interval=1)
            psutil.disk_usage(check_os())
            psutil.virtual_memory()
            time.sleep(1)
    except KeyboardInterrupt:
            print("\nAborting...")



