import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from colorama import Fore, Style, init

init(autoreset=True)

def check_link(name, url, show_missed):
    with open(name, 'r') as fichier:
        for line in fichier:
            word = line.strip()
            if word:
                file_url = f"{url}/{word}.txt"
                try:
                    response = requests.head(file_url)
                    if response.status_code == 404:
                        if show_missed:
                            print(Fore.RED + f"{word} [404] - Not Found")
                    elif response.status_code == 500:
                        if show_missed:
                            print(Fore.BLUE + f"{word} [500] - Internal Server Error")
                            print(Fore.BLUE + f"Response Text: {response.text}")
                    else:
                        print(Fore.GREEN + f"{word} [{response.status_code}] - Exists")
                except requests.exceptions.RequestException as e:
                    if show_missed:
                        print(Fore.RED + f"{word} [ERROR: {e}]")

def check_word(name, url, show_missed):
    with open(name, 'r') as fichier:
        for line in fichier:
            word = line.strip()
            if word:
                m = MultipartEncoder(fields={'code': word})
                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br, zstd',
                    'accept-language': 'fr-FR,fr;q=0.8',
                    'content-type': m.content_type,
                    'origin': 'https://thisisnotawebsitedotcom.com',
                    'referer': 'https://thisisnotawebsitedotcom.com/',
                    'sec-ch-ua': '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'sec-gpc': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
                }
                try:
                    response = requests.post(url, data=m, headers=headers)
                    if response.status_code == 404:
                        if show_missed:
                            print(Fore.RED + f"{word} [404] - Not Found")
                    elif response.status_code == 500:
                        if show_missed:
                            print(Fore.BLUE + f"{word} [500] - Internal Server Error")
                            print(Fore.BLUE + f"Response Text: {response.text}")
                    else:
                        print(Fore.GREEN + f"{word} [{response.status_code}] - Exists")
                except requests.exceptions.RequestException as e:
                    if show_missed:
                        print(Fore.RED + f"{word} [ERROR: {e}]")

def main():
    name = 'input.txt'
    mystery_url = 'https://mystery.thisisnotawebsitedotcom.com/'
    files_url = 'https://files.thisisnotawebsitedotcom.com/is-it-time-yet'
    codes_url = 'https://codes.thisisnotawebsitedotcom.com/'

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, name)

    header = "Gravity Falls ARG : Bill Word Finder\nVers 3.0, by Ababoude (X : @ababoude_)"
    header_line = '-' * len(header)
    print(Fore.YELLOW + header)
    print(Fore.YELLOW + header_line)

    print(Fore.CYAN + "Select an option:")
    print(Fore.CYAN + "1. Bruteforce Submit Bar")
    print(Fore.CYAN + "2. Bruteforce Mystery URL")
    print(Fore.CYAN + "3. Bruteforce Computer codes"+Fore.MAGENTA + " [NEW]")

    choice = input("Enter the number of your choice: ").strip()

    show_missed = input("Do you want to display missed results? (y/n): ").strip().lower() == 'y'

    if choice == '1':
        print(Fore.CYAN + "\nChecking words in mystery URL...\n" + Fore.RESET)
        check_word(file_path, mystery_url, show_missed)
    elif choice == '2':
        print(Fore.CYAN + "\nChecking if files exist...\n" + Fore.RESET)
        check_link(file_path, files_url, show_missed)
    elif choice == '3':
        print(Fore.CYAN + "\nChecking if computer have codes...\n" + Fore.RESET)
        check_word(file_path, codes_url, show_missed)
    else:
        print(Fore.RED + "Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
