import sys
import os
import json
import subprocess

def nmap_ping_sweep(IP_RANGE):
    os.system("nmap " + IP_RANGE + " -sP")