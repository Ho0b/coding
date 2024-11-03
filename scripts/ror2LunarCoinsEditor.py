from sys import argv
from bs4 import BeautifulSoup
import os
import sys

# print("please find your Risk of Rain 2 save file")

fileLocation = "C:\\Users\\netra\\OneDrive\\Desktop\\ror2Save"
os.chdir(fileLocation)

availableFiles = os.listdir(fileLocation)
print("you have:", len(availableFiles), "files, they are \n")
count = 0
for items in availableFiles:
    count += 1
    print((count),items)

print("")

# assigning current ror2 save file
fileNumber = int(input("select the a file using number keys: "))
saveFile = availableFiles[fileNumber-1]
print(saveFile)
fileName, fileExt = os.path.splitext(saveFile)

if fileExt != ".xml":
    print("ERROR: please select a file with the .xml extention")
else:
    with open(saveFile, 'r') as f:
        data = f.read()

    bs_data = BeautifulSoup(data, "xml")

    coinsTag = bs_data.find('coins')
    print(coinsTag)

    bs_data.get_text
    print(coinsTag)
