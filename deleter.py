import os

directory = '/home/ferret/Загрузки/'

os.chdir(directory)

files = [i for i in os.listdir() if '[mangalib.me]' in i]
for i in files:
    os.remove(i)