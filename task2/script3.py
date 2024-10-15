#!/usr/bin/python3
import sys
import os

dir_path: str = sys.argv[1]
count: int = 0

print("Содержимое каталога:")

for filename in os.listdir(dir_path):
    print(filename)

    if os.path.isfile(f"{dir_path}/{filename}"):
        count += 1

print(' '.join([
    '\nКоличество файлов:',
    str(count)
]))


