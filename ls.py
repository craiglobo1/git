import os
import sys

option = str(sys.argv[1])
folder = str(sys.argv[2])
if option == '1':
    path = f'F:\craigComp\Programming\{folder}'
    for items in os.listdir(path):
        print(items)
elif option == '0':
    for items in os.listdir(folder):
        print(items)