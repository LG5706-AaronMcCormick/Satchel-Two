# Satchel:Two CLI startup script
# This serves two purposes: Look pretty and open the next script. I am lazy

# Libraries

import subprocess
import sys
import os

# Checking for internet connectivity on startup

result = subprocess.run(
    ["ping", "-c", "1", "8.8.8.8"] if subprocess.os.name != "nt" else ["ping", "-n", "1", "8.8.8.8"], #Pinging Google's DNS
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

if result.returncode == 0: #If no packets return,
    print("")
else:
    raise Exception("EXCEPTION OCCURED: Connection failed! Please check your internet connectivity!") #Raise an exception

print(r"  _________       __         .__           .__       ___________               _________ .____    .___ ")
print(r" /   _____/____ _/  |_  ____ |  |__   ____ |  |   /\ \__    ___/_  _  ______   \_   ___ \|    |   |   |")
print(r" \_____  \\__  \\   __\/ ___\|  |  \_/ __ \|  |   \/   |    |  \ \/ \/ /  _ \  /    \  \/|    |   |   |")
print(r" /        \/ __ \|  | \  \___|   Y  \  ___/|  |__ /\   |    |   \     (  <_> ) \     \___|    |___|   |")
print(r"/_______  (____  /__|  \___  >___|  /\___  >____/ \/   |____|    \/\_/ \____/   \______  /_______ \___|")
print(" ")
print("Welcome to Satchel:Two CLI!")

if sys.platform == "win32":
    os.system("python main.py")
else:
    os.system("python3 main.py")