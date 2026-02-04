# SatchelFetch CLI Assignments
# A command line tool for viewing assignments!
# ProjectSCR 2026

import pandas as pd
import sys
import os

pd.set_option('display.max_colwidth', None)

calendarlocation = 0

if sys.platform == "win32":
    calendarlocation = "%APPDATA%/Local/SatchelFetch/Download/cleaned.csv"
elif sys.platform == "darwin" or "linux":
    calendarlocation = os.path.expanduser("~/Satchelfetch/Download/cleaned.csv")
else:
    raise Exception("Sorry, whatever obscure platform you're using is not supported!")


if os.path.exists(calendarlocation) == False:
    raise Exception("You have not setup your calendar token! Please return to the main script and select 'Setup Account'.")

df = pd.read_csv(calendarlocation, usecols=["Class Name", "Homework Title", "Set By", "Set On", "Due On"])
print(df)
os.system("python3 main.py")