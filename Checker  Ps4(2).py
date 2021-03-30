import random
from colored import fg
import requests
import sys
import sys as n
import os
import time as mm
import json
import time
from colorama import Fore, init
#TweakPY
color3 = fg(2)
color1 = fg(1)
color2 = fg(50)
colooor = fg(1)
green_color = "\033[1;93m"
O = '\033[33m'  # orange
detect_color = "\033[m"
red_color = "\033[m"
end_banner_color = "\33[00m"
C = "\033[0m"
W = "\033[96m"
BRed="\033[1;31m"
Green="\033[0;36m"
Yellow="\033[0;33m"
count = 0
def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 200)
print('''
   _____ _    _ ______ _____ _  ________ _____    _____   _____ _  _
  / ____| |  | |  ____/ ____| |/ /  ____|  __ \  |  __ \ / ____| || |
 | |    | |__| | |__ | |    | ' /| |__  | |__) | | |__) | (___ | || |_
 | |    |  __  |  __|| |    |  < |  __| |  _  /  |  ___/ \___ \|__   _|
 | |____| |  | | |____ |____| . \| |____| | \ \  | |     ____) |  | |
  \_____|_|  |_|______\_____|_|\_\______|_|  \_\ |_|    |_____/   |_|

                       Coded by | @TweakPY


''')

print(" ")
time.sleep(1)
slow("- Checker Ps4")
print(" ")
time.sleep(1)
print(" ")
username = 'user.txt'
file = open(username).read().splitlines()
for file in file:
	try:
		response = requests.post('https://accounts.api.playstation.com/api/v1/accounts/onlineIds', json={"onlineId": file, "reserveIfAvailable": False})
	except Exception as e:
		print(str(e))
		pass
	if response.status_code == 400:
            count += 1
            print("{}: {}".format(count, file.strip()) + " | NoT Available")
	elif response.status_code == 201:
            count += 1
            print("{}: {}".format(count, file.strip()) + " | Available")
            with open('usersfound.txt', 'a') as x:
                x.write(file + '\n')
	else:
		print(response.status_code)
		print(response.content)


#TweakPY
