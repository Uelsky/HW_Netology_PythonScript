#!/usr/bin/python3
import sys
import os


obj = sys.argv[1]

if os.path.isdir(obj):
    print(f"{obj} - dir")
elif os.path.isfile(obj):
    print(f"{obj} - file")
else:
    print(f"{obj} - not exist")