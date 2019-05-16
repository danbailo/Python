from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('./instancias') if isfile(join('./instancias', f))]

print(onlyfiles)
