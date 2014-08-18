#!/usr/bin/env python3

"""
Program in Python3 to create ZIP files
"""

from sys import argv
from zipfile import ZipFile
import os.path
import argparse

def zipping(in_file, out_file):
    '''Compresses files into ZIP form.

    in_file ==> the input file to be compressed
    out_file ==> the output zip file

    '''
    with ZipFile(out_file, 'w') as myzip:
        for i in in_file:
            myzip.write(i)
            print("done")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--force", help="force action", action="store_true")
    parser.add_argument('oput', help="path of the output zip file")
    parser.add_argument('iput', nargs='+', help="one or more input files")
    args = parser.parse_args()

    ip = args.iput
    op = args.oput

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
