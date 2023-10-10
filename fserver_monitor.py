# fake server monitor script

import random
import time
from colorama import Fore, Style

def generate_cpu_usage():
    return round(random.uniform(3, 100), 2)

def generate_memory_usage():
    return round(random.uniform(2, 8), 2)

def generate_disk_usage():
    return round(random.uniform(0, 100), 2)

def generate_network_latency():
    return round(random.uniform(15, 200), 2)

def print_server_metrics(server_name):
    print(f"{Fore.GREEN}----- {server_name} Monitoring -----{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}CPU Usage: {Style.RESET_ALL}{generate_cpu_usage()}%")
    print(f"{Fore.YELLOW}Memory Usage: {Style.RESET_ALL}{generate_memory_usage()} GB")
    print(f"{Fore.YELLOW}Disk Usage: {Style.RESET_ALL}{generate_disk_usage()}%")
    print(f"{Fore.YELLOW}Network Latency: {Style.RESET_ALL}{generate_network_latency()} ms")
    print(f"{Fore.GREEN}-----------------------------{Style.RESET_ALL}")

while True:
    print(f"{Fore.CYAN}__________ SERVER MONITORING __________{Style.RESET_ALL}")
    print_server_metrics("Server 1")
    print_server_metrics("Server 2")
    print_server_metrics("Server 3")
    print_server_metrics("Server 4")
    print(f"{Fore.CYAN}---------------------------------------{Style.RESET_ALL}")

    print(f"{Fore.MAGENTA}__________ SCRIPT _________________{Style.RESET_ALL}")
    print(f"server 1 : {Fore.GREEN}ON{Style.RESET_ALL}")
    print(f"server 2 : {Fore.GREEN}ON{Style.RESET_ALL}")
    print(f"server 3 : {Fore.GREEN}ON{Style.RESET_ALL}")
    print(f"server 4 : {Fore.RED}OFF{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}---------------------------------------{Style.RESET_ALL}")

    time.sleep(5)
