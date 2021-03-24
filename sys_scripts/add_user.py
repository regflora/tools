#!/usr/bin/env python3
#script to create users in linux

import os
import sys
import subprocess
import getpass

def adduser(username,passw):
    try:
        #useradd command - adds entry to /etc/passwd, /etc/shadow, /etc/group, /etc/gshadow
        # -G to add to specific groups: sudo useradd -g users -G wheel,developers username
        subprocess.run(['useradd', '-p', passw, username ]) 
    except:
        print("Error: Unable to add user.")
        sys.exit()


def main():
    username = input("Enter username: ")
    passw = getpass.getpass()
    adduser(username,passw)

main()
