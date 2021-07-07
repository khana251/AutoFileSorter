#Sort files based on the file extension
#Author: Amaan Ahmad Khan
import os
import shutil

sourceFolder = input(r"Enter source folder, eg: C:\Users\JohnAppleseed\Desktop\sourceFolder:")
destinationFolder = input(r"Enter destination folder, may or may not be same as source folder:")

#sourceFolder = r'Replace this with the location of files eg: C:\Users\JohnAppleseed\Desktop\sourceFolder'
#destinationFolder = r'Replace this with the location where sorted files should be (can be same as sourceFolder)'
sourceFiles = os.listdir(sourceFolder)

for file in sourceFiles:
    name, ext = os.path.splitext(os.path.join(sourceFolder, file))
    destinationPaths = os.path.join(destinationFolder, ext)
    try:
        os.makedirs(destinationPaths)
        shutil.move(os.path.join(sourceFolder, file), os.path.join(destinationPaths, file))
        print(file + " Moved to " + destinationPaths)
    except:
        shutil.move(os.path.join(sourceFolder, file), os.path.join(destinationPaths, file))
        print(file + " Moved to " + destinationPaths)
