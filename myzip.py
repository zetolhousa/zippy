#!/usr/bin/env python3

"""
Program in Python3 to create ZIP files
"""

from sys import argv
from zipfile import ZipFile
import os.path

def zipping():
    with ZipFile(argv[1], 'w') as myzip:
        n = argv[1::]
        for i in n:
            myzip.write(i)
            print("done")

if len(argv) <= 2:
    print("Please enter correct number of arguments: ./myzip.py ../zipfile ../file")
elif os.path.isfile(argv[1]):
    print("The file already exists. Do you want to overwrite? y/n")
    ans = input("=>")
    if ans == 'y':
        zipping()
    else:
        print("Try another name")
else:
    zipping()

