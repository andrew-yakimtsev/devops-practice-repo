import getpass, uptime, datetime, shutil, os

username = getpass.getuser()

def uptime_time():
    seconds_since_boot = int(uptime.uptime())
    hours, remainder = divmod(seconds_since_boot, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} hours {minutes} minutes"

def disk_usage():
    total, used, free = shutil.disk_usage('/')
    disk_percentage = (used / total) * 100
    return disk_percentage

print(f"User: {username}")
print(f"Uptime: {uptime_time()}")
print(f"Disk Usage: {disk_usage():.2f}%")
print(f"Current Dir: {os.getcwd()}")