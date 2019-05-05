#copy all data from one file to another
with open('pyFile.txt', 'r') as readObj:
    with open('copyFile.txt', 'w') as obj:
        obj.write(readObj.read())

#delete file content
with open('pyFile.txt', 'w') as obj:
    pass

#or delete this way
open('pyFile.txt', 'w').close()