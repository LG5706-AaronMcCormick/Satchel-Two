# SatchelFetch CLI Mainscript
# Take control of your homework!
# ProjectSCR 2026

import subprocess
import os

def mainmenu():
    print("Main menu:")
    print("1. Assignments")
    print("2. Setup account")
    print("3. Exit")
    menuSelect = int(input("Please type the corresponding number for your option choice: "))
    if menuSelect == 3:
        exit()
    elif menuSelect == 2:
        os.system("python3 fetch.py")
    elif menuSelect == 1:
        os.system("python3 assignments.py")
    

result = subprocess.run(
    ["ping", "-c", "1", "8.8.8.8"] if subprocess.os.name != "nt" else ["ping", "-n", "1", "8.8.8.8"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

if result.returncode == 0:
    print("")
else:
    raise Exception("EXCEPTION OCCURED: Connection failed! Please check your internet connectivity!")

mainmenu()