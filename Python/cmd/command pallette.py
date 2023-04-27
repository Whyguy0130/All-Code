# I don't know what I am going to do! ## It is supposed to be a cmd like script! #
import subprocess
import time
import psutil
import requests


print("v4.24.2023")
time.sleep(1)
print("Type 'help' to get Started")
time.sleep(1)
a = input(">")
while a == 'help':
    print("List of commands:")
    print("download")
    print("time")
    print("date")
    print("sysinfo")
    print("netusage")
    print("netsh")
    a = input(">")
    if a == 'download':
        url = input("Enter the url>")
        print("Go To <File Extensions> For Help>")
        b = input("Enter a name for the file and the file extension>")
        r = requests.get(url, allow_redirects=True)
        open(b, 'wb').write(r.content)

    elif a == 'time':
        print("The time is:", time.strftime('%I:%M %p'))

    elif a == 'hotkey':
        open(r"C:\\Users\\KittellWyL\\AppData\\Local\\Programs\\AutoHotkey\\UX\\AutoHotkeyUX.exe")

    elif a == 'date':
        print("The date is:", time.strftime('%m/%d/%Y'))

    elif a == 'netsh':
            subprocess.run('netsh')
                           
    elif a == 'sysinfo':
        subprocess.run('systeminfo')

    elif a == 'netusage':
        UPDATE_DELAY = 0.3

        def get_size(bytes):
            for unit in ['', 'K', 'M', 'G', 'T', 'P']:
                if bytes < 1024:
                    return f"{bytes:.2f}{unit}B"
                bytes /= 1024
        io = psutil.net_io_counters()
        bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv
        while True:
            time.sleep(UPDATE_DELAY)
            time.sleep(UPDATE_DELAY)
            io_2 = psutil.net_io_counters()
            us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
            print(f"Upload: {get_size(io_2.bytes_sent)}   "
                 f", Download: {get_size(io_2.bytes_recv)}   "
                 f", Upload Speed: {get_size(us / UPDATE_DELAY)}/s   "
                 f", Download Speed: {get_size(ds / UPDATE_DELAY)}/s      ", end="\r")
            bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
    
    elif a == quit:
        break