import os
import requests
import threading
import concurrent.futures
import time
import socket
import socks
from datetime import datetime
from colorama import Fore, Style
from pystyle import Write, System, Colors

# KETTİP ASCII Art
ascii_art = """

 _        _______ ___________________________ _______ 
| \    /\(  ____ \\__   __/\__   __/\__   __/(  ____ ) 
|  \  / /| (    \/   ) (      ) (      ) (   | (    )|
|  (_/ / | (__       | |      | |      | |   | (____)|
|   _ (  |  __)      | |      | |      | |   |  _____)
|  ( \ \ | (         | |      | |      | |   | (      
|  /  \ \| (____/\   | |      | |   ___) (___| )      
|_/    \/(_______/   )_(      )_(   \_______/|/       

Kettip Scripts Tools

 NOT: Miktar belirlemeyi ayarlamayı unuttum 99  99 99 girebilirsiniz                        
"""
discord_link = "discord https://discord.gg/msNr2fPaTP"

# Renkler
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT

def update_title(scraped_counts):
    title = f"\n{ascii_art}\n{discord_link}\n\n"
    for key, value in scraped_counts.items():
        title += f"[ KETTİP ] {key}: {value} | "
    title = title[:-3]  
    set_terminal_title(title)

def set_terminal_title(title):
    if os.name == 'posix':  
        print(f'\033]0;{title}\007', end='', flush=True)
    elif os.name == 'nt':  
        os.system(f'title {title}')


http_links = [
    "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",

]

socks4_list = [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4",

]

socks5_list = [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",

]

proxy_types = {
    "HTTP_s": http_links,
    "SOCKS4": socks4_list,
    "SOCKS5": socks5_list
}

def get_check_counts():
    counts = {}
    for proxy_type, links in proxy_types.items():
        count = int(input(f"Kaç adet {proxy_type} proxy kontrol edilsin? "))
        counts[proxy_type] = count
    return counts

def print_colored(text, color=reset):
    print(color + text + reset)

def check_proxies(proxy_type, links, count):
    proxies = []
    num_threads = min(100, count)

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(lambda link: scrape_proxy_links(proxy_type, link), links[:count])
        for result in results:
            proxies.extend(result)

    filename = f"{proxy_type.lower()}_proxies.txt"
    with open(filename, "w") as file:
        for proxy in proxies:
            if ":" in proxy and not any(c.isalpha() for c in proxy):
                file.write(proxy + '\n')

    return len(proxies)

def scrape_proxy_links(proxy_type, link):
    proxies = []
    try:
        response = requests.get(link)
        if response.status_code == 200:
            proxies = response.text.splitlines()
            for proxy in proxies:
                print_colored(f"[{proxy_type}] Proxy: {proxy} | Durum: Başarılı", green)
    except requests.RequestException as e:
        print_colored(f"[{proxy_type}] Hata: {e}", red)

    return proxies

def main():

    System.Clear()
    Write.Print(ascii_art, Colors.red_to_blue, interval=0.000)
    print(discord_link)
    time.sleep(3)

    counts = get_check_counts()

    scraped_counts = {}
    for proxy_type, links in proxy_types.items():
        count = counts.get(proxy_type, 0)
        scraped_count = check_proxies(proxy_type, links, count)
        scraped_counts[proxy_type] = scraped_count

    update_title(scraped_counts)

    input("\n\nProgram sonlandı, çıkmak için enter tuşuna basın.")

if __name__ == "__main__":
    main()
