import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from colorama import Fore, Style, init
import itertools

init(autoreset=True)

AUTHOR = "Ababoude (X : Ababoude)"
VERSION = "3.1"
CONTRIBUTORS = ["yBeta (Discord: @ybeta)"]
FILENAME = 'input.txt'
TOOLS = [
    {"name" : "Bruteforce Submit Bar", "newest" : False, "function" : "check_word", "isResulting" : True},
    {"name" : "Bruteforce Mystery URL", "newest" : False, "function" : "check_link", "isResulting" : True},
    {"name" : "Bruteforce Computer codes", "newest" : True, "function" : "check_word", "isResulting" : True},
    {"name" : "Generate possible Combinations", "newest" : True, "function" : "save_combinations_to_file", "isResulting" : False},
]

CHAR_SET = "abcdefghijklmnopqrstuvwxyz0123456789?"
SCRIPT_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(SCRIPT_DIR, FILENAME)

def generate_combinations(max_length):
    """ 
    EN : Generate all possible combinations up to max_length using CHAR_SET.
    FR : Générer toutes les combinaisons possibles jusqu'à max_length en utilisant CHAR_SET.
    """
    for length in range(1, max_length + 1):
        for combination in itertools.product(CHAR_SET, repeat=length):
            yield ''.join(combination)

def save_combinations_to_file(max_length, filename):
    """ 
    EN : Save all combinations up to max_length to a file.
    FR : Enregistrer toutes les combinaisons jusqu'à max_length dans un fichier.
    """
    print(Fore.GREEN + "Generating all possible combinations to file 'input.txt'...")
    with open(filename, 'w') as file:
        n = 1
        for combination in generate_combinations(max_length):
            file.write(combination + '\n')
            print ("\033[?25l"+Fore.YELLOW+f"Number of generated words : {n}", end="\r")
            n +=1
        print("\033[?25h", end="")
    print(Fore.GREEN + f"Combinations saved to {filename}")

def save_successful_combination(word):
    """ 
    EN : Append successful combinations to 'success.txt'.
    FR : Ajouter les combinaisons réussies au fichier 'success.txt'.
    """
    with open('success.txt', 'a') as success_file:
        success_file.write(word + '\n')

def check_link(name, url, show_missed):
    """ 
    EN : Check if files exist at given URL based on words in the file.
    FR : Vérifier si des fichiers existent à l'URL donnée en fonction des mots du fichier.
    """
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
                        save_successful_combination(word)
                except requests.exceptions.RequestException as e:
                    if show_missed:
                        print(Fore.RED + f"{word} [ERROR: {e}]")

def check_word(name, url, show_missed):
    """ 
    EN : Check if words in the file are valid at given URL with POST requests.
    FR : Vérifier si les mots du fichier sont valides à l'URL donnée avec des requêtes POST.
    """
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
                        save_successful_combination(word)
                except requests.exceptions.RequestException as e:
                    if show_missed:
                        print(Fore.RED + f"{word} [ERROR: {e}]")

def count_lines(filename):
    """ 
    EN : Count the number of lines in a text file
    FR : Compte le nombre de lignes dans un fichier texte
    """
    with open(filename, 'r') as file:
        count = 0
        for _ in file:
            count += 1
    return count

def menu(title):
    """ 
    EN : Function to display redundant menus and menus.
    FR : Fonction pour afficher les menus et phrases redondantes.
    """
    if title.lower() == "title":
        os.system('cls' if os.name == 'nt' else 'clear')
        header = "Vers " + VERSION + ", by " + AUTHOR + " | Contributers: " + ";".join(CONTRIBUTORS)
        color = Fore.YELLOW

        print(color + "Gravity Falls ARG : Bill Word Finder")
        print(color + header)
        print(color + '-' * len(header))
    elif title.lower() == "tools":
        n = 1
        menu("loaded")
        for tool in TOOLS:
            color = Fore.BLUE
            indexColor = Fore.RED
            newestColor = Fore.MAGENTA
            text = indexColor + str(n) + ". " + color + tool["name"]

            if tool["newest"]:
                text += newestColor + " [NEW]"
            print(text)
            n += 1
        print(Fore.RED + f"{len(TOOLS) + 1}. Exit\n")
        while True:
            try:
                index = int(input("Enter the number of tool to use it : ").strip())
                if index == len(TOOLS) + 1:
                    raise KeyboardInterrupt
                elif index < 1 or index > len(TOOLS):
                    raise IndexError
                return index 
            except KeyboardInterrupt:
                print(Fore.RED + "\nScript interrupted. Exiting...")
                exit()
            except:
                print(Fore.RED + "ERROR : Please enter a valid number.")
    elif title.lower() == "missed":
        while True:
            try:
                show_missed = input("Do you want to display missed results? (y/n): ").strip().lower()
                if show_missed not in ["y", "n"]:
                    raise ValueError
                return show_missed
            except KeyboardInterrupt:
                print(Fore.RED + "\nScript interrupted. Exiting...")
                exit()
            except:
                print(Fore.RED + "ERROR : Please enter a valid response (y or n).")
    elif title.lower() == "combinations":
        max_length = int(input("Enter the maximum length for combinations: ").strip())
        return max_length
    elif title.lower() == "loaded":
        text = "Words Loaded : "+str(count_lines(FILE_PATH))
        print(Fore.GREEN+ "+"+ "-" * (len(text)+2) + "+")
        print(Fore.GREEN + "| " + "Words loaded : "+str(count_lines(FILE_PATH)) + " |")
        print(Fore.GREEN + "+"+ "-" * (len(text)+2) + "+\n")

def main():
    mystery_url = 'https://mystery.thisisnotawebsitedotcom.com/'
    files_url = 'https://files.thisisnotawebsitedotcom.com/is-it-time-yet'
    codes_url = 'https://codes.thisisnotawebsitedotcom.com/'

    menu("title")
    choice = menu("tools")

    if TOOLS[choice-1]["isResulting"] == True :
        show_missed = menu("missed")

    if choice == 1:
        check_word(FILE_PATH, mystery_url, show_missed)
    elif choice == 2:
        check_link(FILE_PATH, files_url, show_missed)
    elif choice == 3:
        check_word(FILE_PATH, codes_url, show_missed)
    elif choice == 4:
        max_length = menu("combinations")
        save_combinations_to_file(max_length, FILE_PATH)

if __name__ == "__main__":
    main()
