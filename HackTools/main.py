import sys
import os
import json
import subprocess
import pen_utils

print("What do you want to do:")
print("1: nmap ping sweep")
choice = input()
if choice == 1:
    one = str(os.system("ip a | grep 192 | cut -d ' ' -f 6 | cut -d '.' -f 1"))
    two = str(os.system("ip a | grep 192 | cut -d ' ' -f 6 | cut -d '.' -f 2"))
    three = str(os.system("ip a | grep 192 | cut -d ' ' -f 6 | cut -d '.' -f 3"))
    IP_RANGE = (one+"."+two+"."+three+".0/24")
    print(IP_RANGE)
    #pen_utils.nmap_ping_sweep(IP_RANGE)
else:
    print("whoops")


