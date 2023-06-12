import subprocess
import platform
import re
from colorama import init, Fore, Style


# Initialize colorama to work with ANSI escape codes
init()

ip_address = "oldschool36.runescape.com"

if platform.system().lower() == "windows":
    ping_command = f"ping {ip_address} -n 1"
else:
    ping_command = f"ping {ip_address} -c 1"

pattern = r"time=(\d+)ms"

while True:
    output = subprocess.Popen(ping_command, stdout=subprocess.PIPE).communicate()[0].decode()

    match = re.search(pattern, output)
    if match:
        ping_time = int(match.group(1))
    else:
        ping_time = None

    if ping_time is not None:
        if ping_time > 300:
            print(f"{Fore.RED}Ping result: {ping_time}ms{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Ping result: {ping_time}ms{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Request timed out{Style.RESET_ALL}")



    