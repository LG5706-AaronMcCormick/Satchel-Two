# SatchelTwo CLI Token Setup
# For advanced users only who want to test experimental features

# Library setup 

import sys
import os
import ssl
from pathlib import Path
import requests
import warnings
import base64

warnings.filterwarnings('ignore')  # Suppress all warnings

# Setting up an ssl context because it gets mad if you don't

ssl._create_default_https_context = ssl._create_unverified_context

#Variables for configuring directories

downloadlocation = 0
calendarlocation = 0
downloadfolder = 0
configlocation = 0

if sys.platform == "win32":
    home = Path.home()
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo"')
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo\Download"')
    downloadlocation = home / "Documents" / "SatchelTwo" / "Download" / "icalendars.ics"
    calendarlocation = home / "Documents" / "SatchelTwo" / "Download" / "icalendars.csv"
    cleanedlocation = home / "Documents" / "SatchelTwo" / "Download" / "cleaned.csv"
    downloadfolder = home / "Documents" / "SatchelTwo" / "Download"
    configlocation = home / "Documents" / "SatchelTwo" / "config.txt"
    tokenlocation = home / "Documents" / "SatchelTwo" / "token.txt"
elif sys.platform == "darwin" or sys.platform == "linux":
    os.system(r"mkdir ~/SatchelTwo/")
    os.system(r"mkdir ~/SatchelTwo/Download/")
    downloadlocation = os.path.expanduser("~/SatchelTwo/Download/icalendars.ics")
    calendarlocation = os.path.expanduser("~/SatchelTwo/Download/icalendars.csv")
    cleanedlocation = os.path.expanduser("~/SatchelTwo/Download/cleaned.csv")
    downloadfolder = os.path.expanduser("~/SatchelTwo/Download/")
    configlocation = os.path.expanduser("~/SatchelTwo/config.txt")
    tokenlocation = os.path.expanduser("~/SatchelTwo/token.txt")
else:
    raise Exception("Sorry, whatever obscure platform you're using is not supported!") #Throwing an error for those who try running SatchelTwo on some random device.

# Using the base64 decode to get the UID from the token

printurl = input("Enter the URL you copied from the print homework button: ")
auth = printurl[65:289]
decoded = str(base64.b64decode(auth))
studenttoken = decoded[10:18]
expiry = decoded[46:55]
print("")

# Whole bunch of URL stuff to send for specific headers using the token and response

url = ("https://api.satchelone.com/api/students/" + studenttoken)
params = {
    "include": "user_private_info"
}

headers = {
    "Accept": "application/smhw.v2021.5+json",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.satchelone.com/todos/upcoming",
    "X-Platform": "web",
    "Authorization": ("Bearer" + auth ),
    "Origin": "https://www.satchelone.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "If-None-Match": 'W/"72d6b5ac5b8eec8c5f5ce2e0d1f5979a"',
    "User-Agent": (
        "python-requests/2.32.5"
    ),
}

response = requests.get(url, headers=headers, params=params)

# Raise an exception for HTTP errors
response.raise_for_status()

# Parse the JSON response from the SatchelOne API
data = response.json()

# Get the headers, you know the rules. (AND SO DO I!)

response = requests.get(url, headers=headers, params=params)
response.raise_for_status()
data = response.json()

# Getting that info from the response JSON
upi = data.get("user_private_infos", [{}])[0]

email = upi.get("email")
username = upi.get("username")

print("Your email must be", email)
print("And that means your username is", username)
print("Your Student ID (UID) is : ", studenttoken)
print("")
print("Your Authentication Token is: ", auth)
print("")
print("Token setup successful! You will now be returned to the main menu.")

if sys.platform == "win32":
    os.system("python main.py")
else:
    os.system("python3 main.py")
