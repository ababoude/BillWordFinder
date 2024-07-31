import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from colorama import Fore, Style, init

init(autoreset=True)

def read(name, url, show_missed):
    with open(name, 'r') as fichier:
        for line in fichier:
            word = line.strip()
            if word:
                # Create the payload using MultipartEncoder
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
                            print(Fore.RED + f"{word} [404]")
                    elif response.status_code == 500:
                        if show_missed:
                            print(Fore.BLUE + f"{word} [500] - Internal Server Error")
                            print(Fore.BLUE + f"Response Text: {response.text}")
                    else:
                        print(Fore.GREEN + f"{word} [{response.status_code}]")
                except requests.exceptions.RequestException as e:
                    if show_missed:
                        print(Fore.RED + f"{word} [ERROR: {e}]")

def main():
    name = 'input.txt'
    url = 'https://mystery.thisisnotawebsitedotcom.com/'

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, name)

    header = "Gravity Falls ARG : Bill Word Finder\nVers 1.1, by Ababoude (X : @ababoude_)"
    header_line = '-' * len(header)
    print(Fore.YELLOW + header)
    print(Fore.YELLOW + header_line)

    # Ask the user if they want to show missed results
    show_missed = input("Do you want to display missed results ? (y/n): ").strip().lower() == 'y'

    read(file_path, url, show_missed)

if __name__ == "__main__":
    main()
