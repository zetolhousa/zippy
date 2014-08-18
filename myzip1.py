#!/usr/bin/env python3

"""
Program in Python3 to create ZIP files
"""

from sys import argv
from zipfile import ZipFile
import os.path
import argparse

# function taking in input file to zip it into output file
def zipping(in_file, out_file):
    with ZipFile(out_file, 'w') as myzip:
        myzip.write(in_file)
        print("done")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--force", help="force action", action="store_true")
    parser.add_argument("Zipfile", help="path of the output zip file")
    parser.add_argument("Source", help="path(s) of the input files")
    args = parser.parse_args()

    ip = args.Source
    op = args.Zipfile

    if args.force:
        zipping(ip, op)
    elif os.path.isfile(op):
        print("The file already exists. Do you want to overwrite? y/n")
        ans = input("=>")
        if ans == 'y':
            zipping(ip, op)
        else:
            print("Try another name")
    else:
        zipping(ip, op)

if __name__ == '__main__':
    main()
