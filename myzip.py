#!/usr/bin/env python3
from sys import argv
from zipfile import ZipFile

with ZipFile(argv[1], 'w') as myzip:
    n = argv[1::]
    for i in n:
        myzip.write(i)
        print("done")
