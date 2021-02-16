import zipfile
import os


directory = '/home/ferret/manga/тирания_вооружённых'
os.chdir('/home/ferret/Загрузки/')


files = sorted([i for i in os.listdir() if '[mangalib.me]' in i], key=lambda x: (float(x.split()[-4]), float(x.split()[-2])))
for i in files:
    l = i.split()
    tom = l[-4]
    glava = l[-2]
    print(tom, glava)
    try:
        filez = zipfile.ZipFile(i, 'r')
        if tom not in os.listdir(directory):
            os.mkdir(f'{directory}/{tom}')
        os.mkdir(f'{directory}/{tom}/{glava}')
        filez.extractall(f'{directory}/{tom}/{glava}')
        os.remove(i)
    except:
        pass
