import os
import shutil
from colorama import init, Fore, Style
import time
from tkinter import Tk, filedialog
from tqdm import tqdm
from tkinter.filedialog import askdirectory, askopenfilename
import zipfile
import rarfile

init()


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


ascii_art = r"""

 ____    ______   ___    ___       ____     __    __  ____    __  __  ____    ____       
/\  _`\ /\__  _\ /\_ \  /\_ \     /\  _`\  /\ \  /\ \/\  _`\ /\ \/\ \/\  _`\ /\  _`\     
\ \ \L\ \/_/\ \/ \//\ \ \//\ \    \ \ \/\_\\ `\`\\/'/\ \ \L\ \ \ \_\ \ \ \L\_\ \ \L\ \   
 \ \  _ <' \ \ \   \ \ \  \ \ \    \ \ \/_/_`\ `\ /'  \ \ ,__/\ \  _  \ \  _\L\ \ ,  /   
  \ \ \L\ \ \_\ \__ \_\ \_ \_\ \_   \ \ \L\ \ `\ \ \   \ \ \/  \ \ \ \ \ \ \L\ \ \ \\ \  
   \ \____/ /\_____\/\____\/\____\   \ \____/   \ \_\   \ \_\   \ \_\ \_\ \____/\ \_\ \_\
    \/___/  \/_____/\/____/\/____/    \/___/     \/_/    \/_/    \/_/\/_/\/___/  \/_/\/ /
                                                                                         
                                                                                         

"""

url_text = "BILL CYPHER , HEROIN "
version_text = "ELITE-DRAGON"

def display_header():
    columns, rows = shutil.get_terminal_size(fallback=(80, 20))

    ascii_art_lines = ascii_art.strip().split('\n')
    max_art_width = max(len(line) for line in ascii_art_lines)
    padding_left_art = (columns - max_art_width) // 2

    padding_left_text = 34

    print(Fore.RED + '\n'.join(' ' * padding_left_art + line for line in ascii_art_lines) + Style.RESET_ALL)

    print(Fore.RED + ' ' * padding_left_text + version_text + ' ' * (padding_left_text - 19) + url_text + Style.RESET_ALL)
    print()

def search_in_txt_files():
    clear_console()
    display_header()

    print(f"{Fore.RED}♱{Style.RESET_ALL} Press Enter to select a folder with logs...")
    input()

    Tk().withdraw()
    folder_path = askdirectory()

    if not folder_path:
        print("No folder selected.")
        return

    search_queries = input("\nEnter a search term (For example: steam,epic,lol): ").split(',')
    search_results = {}

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for query in search_queries:
                        if query.strip() in content:
                            if query not in search_results:
                                search_results[query] = []
                            search_results[query].append(file_path)

    result_folder = os.path.join(os.getcwd(), 'result')
    os.makedirs(result_folder, exist_ok=True)

    for query, paths in search_results.items():
        save_path = os.path.join(result_folder, f'{query.strip()}_results.txt')
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(paths))

    for query, paths in search_results.items():
        print(f"{query.strip()} found: {len(paths)}")

    input("\nPress the Enter key to return to the main menu...")


def extract_and_filter_archive():
    clear_console()
    display_header()

    print(f"{Fore.RED}♱{Style.RESET_ALL} Retrieve logs from the country archive (.rar, .zip)")

    search_query = input("\nEnter the country name (example: US): ").strip().lower()

    print("\nPress the Enter key to select the archive...")
    input()
    Tk().withdraw()
    archive_path = askopenfilename(filetypes=[("Archive files", "*.zip;*.rar")])

    if not archive_path:
        print("No archive selected.")
        return

    archive_format = os.path.splitext(archive_path)[1][1:].lower()

    extract_folder = os.path.join(os.getcwd(), 'Extract')
    os.makedirs(extract_folder, exist_ok=True)

    main_folders_saved = 0

    def extract_from_zip(zip_ref):
        nonlocal main_folders_saved
        for file_info in zip_ref.infolist():
            if file_info.is_dir() and search_query in file_info.filename.lower():
                folder_name = file_info.filename.strip('/')
                for f in zip_ref.namelist():
                    if f.startswith(folder_name):
                        zip_ref.extract(f, extract_folder)
                main_folders_saved += 1

    def extract_from_rar(rar_ref):
        nonlocal main_folders_saved
        for file_info in rar_ref.infolist():
            if file_info.isdir() and search_query in file_info.filename.lower():
                folder_name = file_info.filename.strip('/')
                for f in rar_ref.namelist():
                    if f.startswith(folder_name):
                        rar_ref.extract(f, extract_folder)
                main_folders_saved += 1

    if archive_format == 'zip':
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            extract_from_zip(zip_ref)
    elif archive_format == 'rar':
        with rarfile.RarFile(archive_path, 'r') as rar_ref:
            extract_from_rar(rar_ref)
    else:
        print("The archive format is not supported.")
        return

    print(f"\nFound and saved {main_folders_saved} folders in the '{extract_folder}'.")

    input("\nPress the Enter key to return to the main menu...")


def remove_txt_files_by_query():
    clear_console()
    display_header()

    print(f"{Fore.RED}♱{Style.RESET_ALL} Press Enter to select the folder with the logs....")
    input()

    Tk().withdraw()
    folder_path = askdirectory()

    if not folder_path:
        print("No folder selected.")
        return

    search_queries = input("\nEnter the name of the .txt files to be deleted (For example: passwords,domain,system):").split(',')

    removed_files = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            for query in search_queries:
                if file.endswith('.txt') and query.strip().lower() in file.lower():
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    removed_files += 1

    print(f"\n{removed_files} .txt files deleted")

    input("\nPress the Enter key to return to the main menu...")


def remove_folders_by_query():
    clear_console()
    display_header()

    print(f"{Fore.RED}♱{Style.RESET_ALL} Press Enter to select the folder with the logs....")
    input()

    Tk().withdraw()
    folder_path = askdirectory()

    if not folder_path:
        print("No folder selected.")
        return

    search_queries = input("\nEnter the name of the folders to be deleted:").split(',')

    removed_folders = 0
    for dir in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, dir)
        if os.path.isdir(dir_path):
            for query in search_queries:
                if query.strip().lower() in dir.lower():
                    shutil.rmtree(dir_path)
                    removed_folders += 1

    print(f"\n{removed_folders} folders removed.")

    input("\nPress the Enter key to return to the main menu...")


def count_logs_by_region():
    clear_console()
    display_header()
    print("\nCounting logs by region")
    print()
    print(f"{Fore.RED}♱{Style.RESET_ALL} Press Enter to select the folder with the logs....")
    input()
    Tk().withdraw()
    folder_path = askdirectory()

    if not folder_path:
        print("No folder selected.")
        return


    region_count = {}
    for dir in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, dir)
        if os.path.isdir(dir_path):
            region_code = dir[:2].upper()
            if region_code.isalpha():
                if region_code not in region_count:
                    region_count[region_code] = 0
                region_count[region_code] += 1

    for region, count in region_count.items():
        print(f"{region}: {count} folders")

    input("\nPress the Enter key to return to the main menu...")


def normalize_key_with_url(key):
    key = key.lower()
    if key in ['user', 'username', 'login']:
        return 'login'
    elif key in ['pass', 'password']:
        return 'password'
    elif key in ['url', 'host']:
        return 'url'
    return key


def extract_credentials_with_url(file_path):
    with open(file_path, 'r', errors='ignore') as file:
        lines = file.readlines()
        credentials_list = []
        temp_credentials = {}
        for line in lines:
            if ':' in line:
                key, value = map(str.strip, line.split(':', 1))
                key = normalize_key_with_url(key)
                temp_credentials[key] = value
            elif temp_credentials:
                login = temp_credentials.get('login', '')
                password = temp_credentials.get('password', '')
                url = temp_credentials.get('url', '')
                if login and password and url:
                    credentials_list.append(f"{url}:{login}:{password}")
                temp_credentials = {}
        if temp_credentials:
            login = temp_credentials.get('login', '')
            password = temp_credentials.get('password', '')
            url = temp_credentials.get('url', '')
            if login and password and url:
                credentials_list.append(f"{url}:{login}:{password}")
        return credentials_list


def find_password_files(folder_path):
    password_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                password_files.append(os.path.join(root, file))
    return password_files


def read_existing_database(file_path):
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file)


def update_and_filter_database(new_entries, existing_entries):
    new_entries_set = set(new_entries)
    unique_entries = new_entries_set - existing_entries
    non_unique_entries = new_entries_set & existing_entries
    return list(unique_entries), list(non_unique_entries)


def save_database_with_url(database, output_file):
    with open(output_file, 'a') as file:
        for entry in database:
            file.write(f"{entry}\n")


def save_unique_entries(unique_entries, output_file):
    with open(output_file, 'w') as file:
        for entry in unique_entries:
            file.write(f"{entry}\n")


def select_folder_with_url():
    print(f"{Fore.RED}♱{Style.RESET_ALL} Base creation (url:login:pass)")
    print()
    input(f"\n{Fore.RED}🕆{Style.RESET_ALL} Press Enter to select the logs folder...")
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder")
    return folder_path


def create_database_with_url(folder_path):
    database = []
    password_files = find_password_files(folder_path)
    for file_path in tqdm(password_files, desc="Processing files", unit="file"):
        credentials_list = extract_credentials_with_url(file_path)
        database.extend(credentials_list)
    return database


def main_with_url():
    start_time = time.time()
    clear_console()
    display_header()
    folder_path = select_folder_with_url()
    if not folder_path:
        print("Folder not selected.")
        return

    database = create_database_with_url(folder_path)
    existing_database_path = 'result_with_url.txt'
    existing_entries = read_existing_database(existing_database_path)

    unique_entries, non_unique_entries = update_and_filter_database(database, existing_entries)

    save_database_with_url(unique_entries, existing_database_path)

    print(f"\nUnique lines found: {len(unique_entries)}")
    print(f"Non-unique strings found: {len(non_unique_entries)}")

    save_unique = input("Do you want to save unique strings to a separate file? (yes/no): ")
    if save_unique.lower() == 'yes':
        unique_file_path = 'unique_entries_with_url.txt'
        save_unique_entries(unique_entries, unique_file_path)
        print(f"The unique strings are saved to a file: {unique_file_path}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    num_lines_saved = len(unique_entries)
    print(f"\nThe database is saved to a file: {existing_database_path}")
    print(f"Strings saved: {num_lines_saved}")
    print(f"Execution time: {elapsed_time:.2f} seconds")

    input("\nPress the Enter key to return to the main menu...")

def display_menu():
    url_text = "ELITE-DRAGON"
    version_text = "BILL CYPHER"
    menu_options = [
        "",
        f"{Fore.RED}♱{Style.RESET_ALL} 1. Extract logs from the country archive (.rar, .zip).",
        f"{Fore.RED}♱{Style.RESET_ALL} 2. Search for queries in the logs (.txt)",
        f"{Fore.RED}♱{Style.RESET_ALL} 3. Reducing the size of logs (.txt, folders).",
        f"{Fore.RED}♱{Style.RESET_ALL} 4. Counting logs by region (folders)",
        f"{Fore.RED}♱{Style.RESET_ALL} 5. Creating a base (login:pass).",
        f"{Fore.RED}♱{Style.RESET_ALL} 6. Create base (url:login:pass)",
        f"{Fore.RED}♱{Style.RESET_ALL} 7. Exit"
    ]

    ascii_art = r"""

 ____    ______   ___    ___       ____     __    __  ____    __  __  ____    ____       
/\  _`\ /\__  _\ /\_ \  /\_ \     /\  _`\  /\ \  /\ \/\  _`\ /\ \/\ \/\  _`\ /\  _`\     
\ \ \L\ \/_/\ \/ \//\ \ \//\ \    \ \ \/\_\\ `\`\\/'/\ \ \L\ \ \ \_\ \ \ \L\_\ \ \L\ \   
 \ \  _ <' \ \ \   \ \ \  \ \ \    \ \ \/_/_`\ `\ /'  \ \ ,__/\ \  _  \ \  _\L\ \ ,  /   
  \ \ \L\ \ \_\ \__ \_\ \_ \_\ \_   \ \ \L\ \ `\ \ \   \ \ \/  \ \ \ \ \ \ \L\ \ \ \\ \  
   \ \____/ /\_____\/\____\/\____\   \ \____/   \ \_\   \ \_\   \ \_\ \_\ \____/\ \_\ \_\
    \/___/  \/_____/\/____/\/____/    \/___/     \/_/    \/_/    \/_/\/_/\/___/  \/_/\/ /
                                                                                         
                                                                                         

"""

    # Get terminal size
    columns, rows = shutil.get_terminal_size(fallback=(80, 20))

    # Calculate the left padding for centering the ASCII art
    ascii_art_lines = ascii_art.strip().split('\n')
    max_art_width = max(len(line) for line in ascii_art_lines)
    padding_left_art = (columns - max_art_width) // 2

    # Calculate the left padding for centering the URL text and version text
    padding_left_text = 34  # You can adjust this value as desired

    # Print the ASCII art centered and in red color
    print(Fore.RED + '\n'.join(' ' * padding_left_art + line for line in ascii_art_lines) + Style.RESET_ALL)

    # Print the version text and URL text, aligned to the same level
    print(Fore.RED + ' ' * padding_left_text + version_text + ' ' * (padding_left_text - 19) + url_text + Style.RESET_ALL)

    # Print the rest of the menu options
    for option in menu_options:
        print(option)


def normalize_key(key):
    key = key.lower()
    if key in ['user', 'username', 'login']:
        return 'login'
    elif key in ['pass', 'password']:
        return 'password'
    return key


def extract_credentials(file_path):
    with open(file_path, 'r', errors='ignore') as file:
        lines = file.readlines()
        credentials_set = set()
        temp_credentials = {}
        for line in lines:
            if ':' in line:
                key, value = map(str.strip, line.split(':', 1))
                key = normalize_key(key)
                temp_credentials[key] = value
            elif temp_credentials:
                login = temp_credentials.get('login', '')
                password = temp_credentials.get('password', '')
                if login and password:
                    credentials_set.add(f"{login}:{password}")
                temp_credentials = {}
        if temp_credentials:
            login = temp_credentials.get('login', '')
            password = temp_credentials.get('password', '')
            if login and password:
                credentials_set.add(f"{login}:{password}")
        return credentials_set


def find_password_files(folder_path):
    password_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                password_files.append(os.path.join(root, file))
    return password_files


def read_existing_database(file_path):
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file)


def update_and_filter_database(new_entries, existing_entries):
    new_entries_set = set(new_entries)
    unique_entries = new_entries_set - existing_entries
    non_unique_entries = new_entries_set & existing_entries
    return list(unique_entries), list(non_unique_entries)


def save_database(database, output_file):
    with open(output_file, 'a') as file:
        for entry in database:
            file.write(f"{entry}\n")


def save_unique_entries(unique_entries, output_file):
    with open(output_file, 'w') as file:
        for entry in unique_entries:
            file.write(f"{entry}\n")


def select_folder():
    print(f"{Fore.RED}♱{Style.RESET_ALL} Creating a base (login:pass)")
    print()
    input(f"\n{Fore.RED}🕆{Style.RESET_ALL} Press Enter to select the logs folder...")
    Tk().withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder")
    return folder_path


def create_database(folder_path):
    database = set()
    password_files = find_password_files(folder_path)
    for file_path in tqdm(password_files, desc="Processing files", unit="file"):
        credentials_set = extract_credentials(file_path)
        database.update(credentials_set)
    return database


def extract_credentials_main():
    start_time = time.time()
    clear_console()
    display_header()
    folder_path = select_folder()
    if not folder_path:
        print("Folder not selected.")
        return

    database = create_database(folder_path)
    existing_database_path = 'result.txt'
    existing_entries = read_existing_database(existing_database_path)

    unique_entries, non_unique_entries = update_and_filter_database(database, existing_entries)

    save_database(unique_entries, existing_database_path)

    print(f"\nUnique lines found: {len(unique_entries)}")
    print(f"Non-unique strings found: {len(non_unique_entries)}")

    save_unique = input("Do you want to save unique strings to a separate file? (yes/no): ")
    if save_unique.lower() == 'yes':
        unique_file_path = 'unique_entries.txt'
        save_unique_entries(unique_entries, unique_file_path)
        print(f"The unique strings are saved to a file: {unique_file_path}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    num_lines_saved = len(unique_entries)

    print(f"\nThe database is saved to a file: {existing_database_path}")
    print(f"Saved lines: {num_lines_saved}")
    print(f"Turnaround time: {elapsed_time:.2f} seconds")

    input("\nPress the Enter key to return to the main menu...")

def reduce_logs():
    clear_console()
    display_header()
    while True:
        print(f"{Fore.RED}♱{Style.RESET_ALL} Reducing the size of logs (.txt, folders).")
        print()
        print(f"{Fore.RED}♱{Style.RESET_ALL} 1. Delete .txt by name")
        print(f"{Fore.RED}♱{Style.RESET_ALL} 2. Delete folders by name")
        print(f"{Fore.RED}♱{Style.RESET_ALL} 3. Return to menu")

        choice = input(f"\n{Fore.RED}🕆{Style.RESET_ALL} Enter your choice: ")

        if choice == '1':
            remove_txt_files_by_query()
        elif choice == '2':
            remove_folders_by_query()
        elif choice == '3':
            break
        else:
            print("\nSFOWARD'S ONLY HERE FOR THREE MINUTES, YOU IDIOT. SIR YES SIR.\n")

def main():
    while True:
        clear_console()
        display_menu()
        choice = input(f"\n{Fore.RED}🕆{Style.RESET_ALL} Enter your choice: ")

        if choice == '1':
            extract_and_filter_archive()
        elif choice == '2':
            search_in_txt_files()
        elif choice == '3':
            reduce_logs()
        elif choice == '4':
            count_logs_by_region()
        elif choice == "5":
            extract_credentials_main()
        elif choice == "6":
            main_with_url()
        elif choice == '7':
            clear_console()
            print("\nGoodbye!\n")
            break
        else:
            clear_console()
            print("\nIncorrect selection. Please enter a number between 1 and 7.\n")


if __name__ == "__main__":
    main()