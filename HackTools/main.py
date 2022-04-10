import sys
import os
import json
import subprocess

def nmap_ping_sweep(IP_RANGE):
    os.system("nmap " + IP_RANGE + " -sP")

print("What do you want to do:\n")
print("1: nmap ping sweep\n")
choice = input()
if choice == '1':
    IP_RANGE = input("what is your IP range: ")
    nmap_ping_sweep(IP_RANGE)
else:
    print("whoops")


